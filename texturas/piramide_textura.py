from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import png

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\033'

# Number of the glut window.
window = 0

# Rotations for cube. 
xrot = yrot = zrot = 0.0
dx = 0.1
dy = 0
dz = 0

def LoadTextures():
    global texture
    texture = [ glGenTextures(1) ]

    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[0])
    reader = png.Reader(filename='textura.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

def InitGL(Width, Height):             
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0) 
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0:                        
        Height = 1
    glViewport(0, 0, Width, Height)      
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def DrawGLScene():
    global xrot, yrot, zrot, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()                   
    glClearColor(0.5,0.5,0.5,1.0)            
    glTranslatef(0.0,0.0,-5.0)
    glRotatef(xrot,1.0,0.0,0.0)          
    glRotatef(yrot,0.0,1.0,0.0)           
    glRotatef(zrot,0.0,0.0,1.0) 
    
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glBegin(GL_TRIANGLES)

    glTexCoord2f(1.0, 0.0); glVertex3f( 0.0, 1.0, 0.0)
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(0.0, 0.0); glVertex3f(1.0, -1.0, 1.0)

    glTexCoord2f(1.0, 0.0); glVertex3f(0.0, 1.0, 0.0)
    glTexCoord2f(0.0, 0.0); glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f(1.0, -1.0, -1.0)

    glTexCoord2f(1.0, 0.0); glVertex3f(0.0, 1.0, 0.0)
    glTexCoord2f(0.0, 1.0); glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)

    glTexCoord2f(1.0, 0.0); glVertex3f( 0.0, 1.0, 0.0)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0,-1.0,-1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,-1.0, 1.0)

    glEnd()                # Done Drawing The Cube
    
    xrot = xrot + 1.0                 # X rotation
    yrot = yrot + 1.0                 # Y rotation
    zrot = zrot + 1.0                 # Z rotation

    glutSwapBuffers()



# def piramide():
#     global quadro
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glPushMatrix()
#     # glRotatef(quadro,0.0,1.0,0.0)
#     glRotatef(90.0+quadro,1.0,0.0,0.0)
#     raio = 0.7
#     n = 6
#     glBegin(GL_TRIANGLES)
#     for i in range(0,n): #Faces
#         glColor3fv(cores[(i)%len(cores)])
#         glVertex3f(0.0,0.0,-1.0)
#         a = (i/n) * 2 * math.pi   
#         x = raio * math.cos(a)
#         y = raio * math.sin(a)
#         glVertex3f(x,y,0.0)
#         a = ((i+1)/n) * 2 * math.pi
#         x = raio * math.cos(a)
#         y = raio * math.sin(a)
#         glVertex3f(x,y,0.0)
#     glEnd()
#     glBegin(GL_TRIANGLE_FAN)
#     glColor3f(0.3,0.3,0.3)
#     glVertex3f(0.0,0.0,0.0)
#     for i in range(0,n+1):
#         a = (i/n) * 2 * math.pi   
#         x = raio * math.cos(a)
#         y = raio * math.sin(a)
#         glVertex3f(x,y,0.0)
#     glEnd()
#     glutSwapBuffers()
#     quadro += 1
#     glPopMatrix()

# def DrawGLScene():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     piramide()
#     glutSwapBuffers()
 

def keyPressed(tecla, x, y):
    global dx, dy, dz
    if tecla == ESCAPE:
        glutLeaveMainLoop()
    elif tecla == b'x' or tecla == b'X':
        dx = 1.0
        dy = 0
        dz = 0   
    elif tecla == b'y' or tecla == b'Y':
        dx = 0
        dy = 1.0
        dz = 0   
    elif tecla == b'z' or tecla == b'Z':
        dx = 0
        dy = 0
        dz = 1.0

def teclaEspecialPressionada(tecla, x, y):
    global xrot, yrot, zrot, dx, dy, dz
    if tecla == GLUT_KEY_LEFT:
        print ("ESQUERDA")
        xrot -= dx                # X rotation
        yrot -= dy                 # Y rotation
        zrot -= dz                     
    elif tecla == GLUT_KEY_RIGHT:
        print ("DIREITA")
        xrot += dx                # X rotation
        yrot += dy                 # Y rotation
        zrot += dz                     
    elif tecla == GLUT_KEY_UP:
        print ("CIMA")
    elif tecla == GLUT_KEY_DOWN:
        print ("BAIXO")

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)    
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Piramide Textura")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    glutSpecialFunc(teclaEspecialPressionada)
    InitGL(640, 480)
    glutMainLoop()

main()












# def timer(i):
#     glutPostRedisplay()
#     glutTimerFunc(50,timer,1)


# # PROGRAMA PRINCIPAL
# glutInit(sys.argv)
# glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
# glutInitWindowSize(800,600)
# glutCreateWindow("PIRAMIDE")
# glutDisplayFunc(piramide)
# glEnable(GL_MULTISAMPLE)
# glEnable(GL_DEPTH_TEST)
# glClearColor(0.,0.,0.,1.)
# gluPerspective(45,800.0/600.0,0.1,100)
# glTranslatef(0.0, 0.0,-5.0)
# glutTimerFunc(50,timer,1)
# glutMainLoop()


