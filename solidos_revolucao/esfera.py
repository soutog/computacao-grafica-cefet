from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *



def esfera():
    glRotatef(1,1,0,0)
    glBegin(GL_POINTS)
    raio = 1
    n = 50

    for i in range(0,n):
        theta = (i*pi/n) - pi/2
        for j in range(0,n):
            phi = (j*2*pi)/n
            x = raio*cos(theta)*cos(phi)
            y = raio*sin(theta)
            z = raio*cos(theta)*sin(phi)
            glVertex3f(x,y,z)
    glEnd()


def desenha():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    esfera()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("ESFERA")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
#              fov  aspect Ratio  nearPlane  farPlane
gluPerspective(45,  800.0/600.0,  0.1,       100.0)
glTranslatef(0.0,0.0,-5)
glutTimerFunc(50,timer,1)
glutMainLoop()