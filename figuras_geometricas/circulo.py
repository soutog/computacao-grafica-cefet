from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
quadro = 0

def desenha():
    global quadro
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLE_FAN)
    glColor3fv(cores[0])
    glVertex2f(0,0)
    raio = 0.7
    n = 60
    for i in range(0,n+7):
        a = (i/n) * 2 * math.pi
        x = raio * math.cos(a)
        y = raio * math.sin(a)
        glColor3fv(cores[(i+1)%len(cores)])
        glVertex2f(x,y)
    glEnd()
    glutSwapBuffers()
    quadro += 1

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("CIRCULO")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glClearColor(0.,0.,0.,1.)
glutMainLoop()


