import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.parser.Feature;
import io.github.cdimascio.dotenv.Dotenv;
import java.io.*;
import java.util.logging.Logger;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.*;
import javax.servlet.annotation.*;

@WebServlet(name = "NoteServlet", urlPatterns = {"
/note
/*"})
public class NoteServlet extends HttpServlet {
    private String secret;
    private static final Logger logger = Logger.getLogger(NoteServlet.class.getName());
    @Override
    public void init() throws ServletException {
        Dotenv dotenv = Dotenv.configure().directory("
/opt
/tomcat") .load();
        secret = dotenv.get("SECRET");

        if (secret == null) {
            throw new ServletException("SECRET env missing!");
        }
    }

    
/ hey, local first, remoter
    private String[] Denlist = new String[]{"TemplatesImpl", "JdbcRowSetImpl","WrapperConnection", "@type", "ldap", "rmi"};

    public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        String path = request.getPathInfo();
        if (path == null || path.length() <= 1) {
            request.setAttribute("errorMessage", "Path is empty!");
            request.getRequestDispatcher("
/dashboard.jsp").forward(request, response);
            return;
        }

        String key = path.substring(1);
        if (key.equals(secret)) {
            String content = RequestContentReader.getContent(request);
            for(String Den : this.Denlist) {
                if (content.contains(Den)) {
                    request.setAttribute("errorMessage", "Hacker!!!!");
                    RequestDispatcher dispatcher = request.getRequestDispatcher("
/dashboard.jsp");
                    dispatcher.forward(request, response);
                    return;
                }
            }
            
/ Currently in the build process, temporarily use the feature with note length <10.
            if (content.length() < 20){
                content = "{ note: \""+ content + "\" }";
            }
            try {
                Object object = JSON.parseObject(content, Object.class, Feature.SupportNonPublicField);
                request.setAttribute("notes", object);
                request.getRequestDispatcher("
/dashboard.jsp").forward(request, response);

            } catch (Exception e) {
                System.out.printf("error:" + "" + e.getMessage() + "\n");
                request.setAttribute("errorMessage", "Something wrong because the system is under development!");
                request.getRequestDispatcher("
/dashboard.jsp").forward(request, response);
            }
        } else {
            logger.info("Incoming request path: " + path);
            request.setAttribute("errorMessage", "Wrong secret!");
            request.getRequestDispatcher("
 dashboard.jsp").forward(request, response);
        }
    }
}