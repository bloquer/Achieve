package control;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.RequestDispatcher;
import control.BoardCommand;
import control.BoardDeleteCommand;
import control.BoardListCommand;
import control.BoardRetrieveCommand;
import control.BoardUpdateCommand;
import control.BoardWriteCommand;


@WebServlet("*.do")
public class BoardFrontController extends HttpServlet {
	
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doPost(request, response);
	}

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		request.setCharacterEncoding("EUC-KR");
		String requestURI = request.getRequestURI();
		String contextPath = request.getContextPath();
		String com = requestURI.substring(contextPath.length());
		
		BoardCommand command = null;
		String nextPage = null;
		
		
		if(com.equals("/writeui.do")) {
			command = new BoardWriteuiCommand();
			command.execute(request, response);
			nextPage = "write.jsp";
		}
		if(com.equals("/write.do")) {
			command = new BoardWriteCommand();
			command.execute(request, response);
			nextPage = "list.do";
		}
		if(com.equals("/list.do")) {
			command = new BoardListCommand();
			command.execute(request, response);
			nextPage = "list.jsp";
		}
		if(com.equals("/retrieve.do")) {
			command = new BoardRetrieveCommand();
			command.execute(request, response);
			nextPage = "retrieve.jsp";
		}
		if(com.equals("/updateui.do")) {
			command = new BoardUpdateuiCommand();
			command.execute(request, response);
			nextPage = "update.jsp";
		}
		if(com.equals("/update.do")) {
		    command = new BoardUpdateCommand();
		    command.execute(request, response);
		    nextPage = "retrieve.do";
		}
		if(com.equals("/delete.do")){
			command = new BoardDeleteCommand();
			command.execute(request, response);
			nextPage = "list.do";
		}
		
		RequestDispatcher dis = request.getRequestDispatcher(nextPage);
		dis.forward(request, response);
	}

}
