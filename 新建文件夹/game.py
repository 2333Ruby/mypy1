import pygame
import sys
from time import sleep
from pygame.locals import *


pygame.init()
pygame.mixer.init()
pygame.display.set_caption('虾跳')
# a=-1
size=width,height=960,640
color = (255, 255, 255)
screen=pygame.display.set_mode(size)
img=pygame.image.load('船.jpg')
img_rect= img.get_rect()
w,h=img.get_size()
print(w, h)
x=(width-w)//2
y=(height-h)//2
# speed=[5,5]

# screen.blit(img,(img_x,img_y))

# pygame.mixer.music.load('pianoC.mp3')
# pygame.mixer.music.play()
# pygame.mixer.music.set_endevent(pygame.USEREVENT)


class Bullet:
    def __init__(self,x,y,screen):
        self.x = x
        self.y = y
        self.window = screen
        self.surface = pygame.image.load('260.jpg')
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()

    def display(self):
        self.window.blit(self.surface,(self.x,self.y))





while True:
    # img_rect=img_rect.midbottom
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            sys.exit()
        # if event.type == KEYUP:#这个要英文输入法，中文的没反应
        #     if event.key == pygame.K_ESCAPE:
        #         sys.exit()
        #     elif event.key == pygame.K_w:
        #         print('w')
    # for event in pygame.event.get():#这个玩意不要写多，写多了会卡循环，除了第一个循环其他的都跑不动
    #     if event.type == pygame.USEREVENT:
    #         pygame.mixer.music.play()
    #     if key_press[K_s]:
    #         print('s')
    #         img_rect.bottom+=10
        press=pygame.key.get_pressed()
        if 1 in press:
            if press[K_a]:
                x -= 20
            if press[K_d]:
                x += 20
            if press[K_s]:
                y += 20
            if press[K_w]:
                y -= 20
            if press[K_q]:
                y -= 40
        if x < 0:
            x = 0
        if x > width-w:
            x=width-w
        if y < 0:
            y = 0
        if y > height-h:
            y = height-h
        # elif event.type == pygame.KEYDOWN:
        #
        #     if event.key == K_a:
        #         print('a')
        #         x -= 20
        #
        #     if event.key == K_w:
        #         print('w')
        #         y -= 20
        #     if event.key == K_d:
        #         print('d')
        #         x += 20
        #     if event.key == K_s:
        #         print('s')
        #         y += 20

    # img_rect = img_rect.move(speed)
    # if img_rect.top <0 or img_rect.bottom >height:
    #     speed[1]=speed[1]*a
    # if img_rect.left <0 or img_rect.right >width:
    #     speed[0]=speed[0]*a
    screen.fill(color)
    screen.blit(img, [x, y])
    pygame.display.flip()
    # sleep(0.1)
