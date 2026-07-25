# Section 08: NFS

Module: 04. Footprinting

---

## Questions & Answers

### 1. Enumerate the NFS service and submit the contents of the flag.txt in the "nfs" share as the answer.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~/target-NFS/mnt/nfsshare]
└──╼ [★]$ cd ../../var/nfs
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~/target-NFS/var/nfs]
└──╼ [★]$ cat flag.txt
HTB{hjglmvtkjhlkfuhgi734zthrie7rjmdze}
```

**Answer:** `HTB{hjglmvtkjhlkfuhgi734zthrie7rjmdze}`

---

### 2. Enumerate the NFS service and submit the contents of the flag.txt in the "nfsshare" share as the answer.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ showmount -e 10.129.134.68
Export list for 10.129.134.68:
/var/nfs      10.0.0.0/8
/mnt/nfsshare 10.0.0.0/8
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ mkdir target-NFS
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ sudo mount -t nfs 10.129.134.68:/ ./target-NFS/ -o nolock
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ cd target-NFS
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~/target-NFS]
└──╼ [★]$ ls
mnt  var
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~/target-NFS]
└──╼ [★]$ cd mnt/nfsshare/
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~/target-NFS/mnt/nfsshare]
└──╼ [★]$ ls
flag.txt
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~/target-NFS/mnt/nfsshare]
└──╼ [★]$ cat flag.txt
HTB{8o7435zhtuih7fztdrzuhdhkfjcn7ghi4357ndcthzuc7rtfghu34}
```

**Answer:** `HTB{8o7435zhtuih7fztdrzuhdhkfjcn7ghi4357ndcthzuc7rtfghu34}`

---

[Back to Module Index](./README.md)
