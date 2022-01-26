from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import numpy as np

phi0 = 0
phin = 2*pi

theta0 = 0
thetan = 2*pi

n = 150
raio = 1
dx = 3

dphi = (phin - phi0)/n
dtheta = (thetan - theta0)/n

def cor(t, c1 = np.array([1,0,0]), c2 = np.array([0,0,1])):
    return c1 + t*(c2 - c1) 

def rosquinha():
    glRotatef(1,1,0,0)

    phi = phi0
    for i in range(0,n):
        glBegin(GL_TRIANGLE_STRIP)
        theta = theta0
        # theta = (i*2*pi)/n
        for j in range(0,n):
            # phi = (j*2*pi)/n
            x = (dx + raio*cos(theta))*cos(phi)
            y = raio*sin(theta)
            z = (dx + raio*cos(theta))*sin(phi)

            x_2 = (dx + raio*cos(theta))*cos(phi+dphi)
            y_2 = raio*sin(theta)
            z_2 = (dx + raio*cos(theta))*sin(phi+dphi)

            glColor3fv(cor(j/(n-1)))

            glVertex3f(x,y,z)
            glVertex3f(x_2,y_2,z_2)

            theta += dtheta
        glEnd()
        phi += dphi


def desenha():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    rosquinha()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("ROSQUINHA")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
#              fov  aspect Ratio  nearPlane  farPlane
gluPerspective(45,  800.0/600.0,  0.1,       100.0)
glTranslatef(0.0,0.0,-20)
glutTimerFunc(50,timer,1)
glutMainLoop()