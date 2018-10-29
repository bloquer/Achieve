#include <gl/glut.h>


GLfloat vertex[][3] = {
	{-1.0,-1.0,1.0},
	{-1.0,1.0,1.0},
	{1.0,1.0,1.0},
	{1.0,-1.0,1.0},
	{-1.0,-1.0,-1.0},
	{-1.0,1.0,-1.0},
	{1.0,1.0,-1.0},
	{1.0,-1.0,-1.0},
};

void
polygon(int a, int b, int c, int d)
{
	glBegin(GL_POLYGON);
	glVertex3fv(vertex[a]);
	glVertex3fv(vertex[b]);
	glVertex3fv(vertex[c]);
	glVertex3fv(vertex[d]);
	glEnd();
}

void
cube()
{
	polygon(0, 3, 2, 1);
	polygon(0, 1, 5, 4);
	polygon(4, 7, 6, 5);
	polygon(7, 6, 2, 3);
	polygon(1, 2, 6, 5);
	polygon(0, 3, 7, 4);
}

void
MyDisplay()
{
	glClear(GL_COLOR_BUFFER_BIT);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	glRotatef(45.0, 0.0, 1.0, 0.0);
	glRotatef(45.0, 0.0, 0.0, 1.0);
	glRotatef(45.0, 1.0, 0.0, 0.0);
	cube();
	glFlush();
}

int
main(int argc, char **argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_RGB);
	glutInitWindowPosition(0, 0);
	glutInitWindowSize(300, 300);	
	glutCreateWindow("a");
	glClearColor(0.0, 0.0, 0.0, 1.0);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-4.0, 4.0, -4.0, 4.0, -4.0, 4.0);
	glutDisplayFunc(MyDisplay);
	glutMainLoop();

	return 0;
}