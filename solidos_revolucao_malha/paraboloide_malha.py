from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import numpy as np

theta0 = 0
thetan = pi

r0 = -2
rf = 2

n = 50

dtheta = (thetan - theta0)/n
dr = (rf-r0)/n


def cor(t, c1 = np.array([1,0,0]), c2 = np.array([0,0,1])):
    return c1 + t*(c2 - c1) 


def paraboloide():
    glRotatef(1,1,0,0)
    
    r = r0
    for i in range(0,n):
        # r = i*(rf-r0)/n + r0
        glBegin(GL_TRIANGLE_STRIP)
        theta = theta0
        for j in range(0,n):
            x = r*cos(theta)
            y = r**2
            z = r*sin(theta)

            x_2 = (r+dr)*cos(theta)
            y_2 = (r+dr)**2
            z_2 = (r+dr)*sin(theta)

            glColor3fv(cor(j/(n-1)))
            
            glVertex3f(x,y,z)
            glVertex3f(x_2,y_2,z_2)

            theta += dtheta
        glEnd()
        r += dr


def desenha():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    paraboloide()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PARABOLOIDE")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
#              fov  aspect Ratio  nearPlane  farPlane
gluPerspective(45,  800.0/600.0,  0.1,       100.0)
glTranslatef(0.0,0.0,-15)
glutTimerFunc(50,timer,1)
glutMainLoop()