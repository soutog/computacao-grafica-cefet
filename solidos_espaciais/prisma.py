from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

a = 0

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def prisma():
    raio = 2
    raio2 = 2
    N = 50
    H = 4
    pontosBase = []
    pontosBase2 = []
    angulo = (2*math.pi)/N

    glPushMatrix()
    glTranslatef(0,-2,0)
    glRotatef(a,0.0,1.0,0.0)
    glRotatef(-110,1.0,0.0,0.0)
    glColor3fv(cores[0])

    # BASE
    glBegin(GL_POLYGON)
    for i in range(0,N):
        x = raio * math.cos(i*angulo)
        y = raio * math.sin(i*angulo)
        pontosBase += [ (x,y) ]
        glVertex3f(x,y,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for j in range(0,N):
        x2 = raio2 * math.cos(j*angulo)
        y2 = raio2 * math.sin(j*angulo)
        pontosBase2 += [(x2,y2)]
        glVertex3f(x2,y2,H)
    glEnd()

    # LATERAL
    glBegin(GL_QUAD_STRIP)
    for i in range(0,N):
        glColor3fv(cores[(i+1)%len(cores)])
        glVertex3f(pontosBase[i][0],pontosBase[i][1],0.0)
        glVertex3f(pontosBase[(i+1)%N][0],pontosBase[(i+1)%N][1],0.0)
        glVertex3f(pontosBase2[i][0],pontosBase2[i][1],H)
        glVertex3f(pontosBase2[(i+1)%N][0],pontosBase2[(i+1)%N][1],H)
    glEnd()

    glPopMatrix()


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    prisma()
    a+=1
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PRISMA")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0,0,0,1)
gluPerspective(70,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-10)
glutTimerFunc(10,timer,1)
glutMainLoop()