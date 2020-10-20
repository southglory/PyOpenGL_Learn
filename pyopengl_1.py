import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# vertices = (
# 3차원 좌표계로 꼭지점 좌표를 나타낸 것. 각 꼭지점의 평균값은 좌표계의 원점이 됨.
vertices = ((1,-1,-1),(1,1,-1),
            (-1,1,-1),(-1,-1,-1),
            (1,-1,1),(1,1,1),
            (-1,-1,1),(-1,1,1))
# edges= ( : 두 꼭지점 좌표를 연결한다. 예를 들어 (0,1)은 첫 번째와 두 번째 꼭지점 좌표를 연결함.
edges = ((0,1), (0,3), (0,4),
         (2,1), (2,3), (2,7),
         (6,3), (6,4), (6,7),
         (5,1), (5,4), (5,7))

def drawCube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


# main
# note:
# gluPerepective(시야각, 종횡비, 근거리 클리핑 평면 위치, 원거리 클리핑 평면 위치)
# glTranslatef(x,y,z) : 인자로 입력된 위치에서 바라보도록 시점 정함. x: 화면의 가로, y = 화면의 세로, z= 화면에서 수직으로 나오는 방향.
# (0.0, 0.0, -7) : 화면 뒤쪽으로 7만큼 뒤.
# glRotatef(각도, x,y,z) : (0,0,0) 위치를 중심으로 (x,y,z) 축방향으로 화면의 모든 물체를 {각도}씩 회전시킴.
# glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) : OpenGL의 모든 버퍼를 비움. 즉, 이전에 그렸던 물체들에 대한 정보를 제거함.
# drawCube(): 새로운 정육면체를 그림.
def myOpenGL():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)


    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)


    glTranslatef(0.0, 0.0, -7)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 0, 100, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        drawCube()
        pygame.display.flip()
        pygame.time.wait(10)

myOpenGL()
