from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *



def rosquinha():
    glRotatef(1,1,0,0)
    glBegin(GL_POINTS)
    raio = 1
    n = 150
    dx = 3

    for i in range(0,n):
        theta = (i*2*pi)/n
        for j in range(0,n):
            phi = (j*2*pi)/n
            x = (dx + raio*cos(theta))*cos(phi)
            y = raio*sin(theta)
            z = (dx + raio*cos(theta))*sin(phi)
            glVertex3f(x,y,z)
    glEnd()


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