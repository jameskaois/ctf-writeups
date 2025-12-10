import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.*;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Enumeration;

@WebFilter("
/note")
public class FilterInput implements Filter {
    private static final String VALID_REGEX = "^[a-zA-Z0-9{}:\u00C0-\u1EF9\"\\s]+$";

    public void init(FilterConfig filterConfig) {
        System.out.println("[*] Filter init");
    }

    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain)
            throws IOException, ServletException {

        HttpServletRequest request = (HttpServletRequest) servletRequest;
        HttpServletResponse response = (HttpServletResponse) servletResponse;
        HttpSession session = request.getSession(false);

        boolean loggedIn = false;
        if (session != null) {
            loggedIn = (session.getAttribute("username") != null);
        }
        if (!loggedIn){
            if(!servletRequest.getParameterNames().hasMoreElements()) {
                request.setAttribute("errorMessage", "Wrong usrname or password!");
                RequestDispatcher dispatcher = request.getRequestDispatcher("
/login.jsp");
                dispatcher.forward(request, response);
                return;
            }
        }
        else {
            Enumeration<String> enumeration = servletRequest.getParameterNames();
            while (enumeration.hasMoreElements()) {
                String parameterName = enumeration.nextElement();
                String paramValue = servletRequest.getParameter(parameterName);
                
/
                if (paramValue == null || !paramValue.matches(VALID_REGEX))  {
                    if (session != null) {
                        session.invalidate();
                    }
                    request.setAttribute("errorMessage", "Do not challenge my filter. Input data must be only a-zA-Z and not null!!!");
                    RequestDispatcher dispatcher = request.getRequestDispatcher("
 login.jsp");
                    dispatcher.forward(request, response);
                    return;
                }
            }

            filterChain.doFilter(servletRequest, servletResponse);
        }
    }

}