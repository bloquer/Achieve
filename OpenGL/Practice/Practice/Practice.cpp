#define NULL 0

#include <gl/glut.h>
#include <stdlib.h>

#define TORSO_HEIGHT 5.0
#define TORSO_RADIUS 1.0
#define UPPER_ARM_HEIGHT 3.0
#define LOWER_ARM_HEIGHT 2.0
#define UPPER_LEG_RADIUS 0.5
#define LOWER_LEG_RADIUS 0.5
#define UPPER_LEG_HEIGHT 2.0
#define LOWER_LEG_HEIGHT 3.0
#define UPPER_ARM_RADIUS 0.5
#define LOWER_ARM_RADIUS 0.5
#define HEAD_HEIGHT 1.5
#define HEAD_RADIUS 1.0

static GLfloat theta[11] = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
			180.0, 0.0, 180.0, 0.0 };
static GLint angle = 2;

GLUquadricObj *t, *h, *lua, *lla, *rua, *rla, *lll, *rll, *rul, *lul;

double size = 1.0;

void
torso()
{
	glPushMatrix();
	glRotatef(-90.0, 1.0, 0.0, 0.0);
	gluCylinder(t, TORSO_RADIUS, TORSO_RADIUS, TORSO_HEIGHT, 10, 10);
	glPopMatrix();
}