import cv2 as cv
import mediapipe as mp
import pygame
import random
import os
import sys
pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
cap = cv.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraw = mp.solutions.drawing_utils
handStylems = mpDraw.DrawingSpec(color= (0,255,0),thickness = 15)
handStylecon = mpDraw.DrawingSpec( color = (0,0,255),thickness = 5)
running = True
score = 0
fps = 60

def reborn():
    r = Enemy()
    x= Enemyx()
    y = ReEnemy()
    z = ReEnemyx()
    all_sprites.add(r)
    all_sprites.add(x)
    all_sprites.add(y)
    all_sprites.add(z)
    enemies.add(x)
    enemies.add(r)
    enemies.add(y)
    enemies.add(z)
def solo_reborn():
    x = random.randint(1,4)
    if x ==1:
        r = Enemy()
        all_sprites.add(r)
        enemies.add(r)
    elif x==2:
        y = Enemyx()
        all_sprites.add(y)
        enemies.add(y)
    elif x==3:
        z = ReEnemy()
        all_sprites.add(z)
        enemies.add(z)
    elif x==4:
        k = ReEnemyx()
        all_sprites.add(k)
        enemies.add(k)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill('green')
        self.rect = self.image.get_rect()
        self.rect.x =200
        self.rect.y = 200
        self.health = 100
    def update(self):
        
        if triggerx:
            self.rect.x -=5
        if detriggerx:
            self.rect.x+=5
        if triggery:
            self.rect.y -=5
        if detriggery:
            self.rect.y+=5
        if self.rect.x >=500-50:
            self.rect.x=500-50
        if self.rect.y >= 500-50:
            self.rect.y = 500-50
        if self.rect.x <=0:
            self.rect.x=0
        if self.rect.y <=0:
            self.rect.y = 0
    def shoot(self):
        bullet = Bullet(self.rect.centerx,self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0,500) 
        self.rect.centery = random.randrange(-100,-30)
        self.speedy = random.randrange(5,13)
        self.speedx = random.randrange(-2,2)
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > 600 or self.rect.left>500 or self.rect.right < 0:
            self.rect.centerx = random.randrange(0,500) 
            self.rect.centery = random.randrange(-100,-30)
            self.speedy = random.randrange(5,13)
            self.speedx = random.randrange(-2,2)
class Enemyx(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.centery = random.randrange(0,500)
        self.rect.centerx = random.randrange(-100,-30)
        self.speedx = random.randrange(5,13)
        self.speedy = random.randrange(-2,2)
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > 500 or self.rect.left>500 or self.rect.bottom<0:
            self.rect.centery = random.randrange(0,500)
            self.rect.centerx = random.randrange(-100,-30)
            self.speedx = random.randrange(5,13)
            self.speedy = random.randrange(-2,2)
class ReEnemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0,500) 
        self.rect.centery = random.randrange(500,560)
        self.speedy = random.randrange(-13,-5)
        self.speedx = random.randrange(-2,2)
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom< 0 or self.rect.left>600 or self.rect.right < -100:
            self.rect.centerx = random.randrange(0,500) 
            self.rect.centery = random.randrange(500,560)
            self.speedy = random.randrange(-13,-5)
            self.speedx = random.randrange(-2,2)
class ReEnemyx(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.centery = random.randrange(0,500) 
        self.rect.centerx = random.randrange(500,560)
        self.speedx = random.randrange(-13,-5)
        self.speedy = random.randrange(-2,2)
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom< 0 or self.rect.left>600 or self.rect.right < -100:
            self.rect.centery = random.randrange(0,500) 
            self.rect.centerx = random.randrange(500,560)
            self.speedx = random.randrange(-13,-5)
            self.speedy = random.randrange(-2,2)
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10))
        self.image.fill('yellow')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedy = random.randrange(-15,15)
        self.speedx = random.randrange(-15,15)
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > 500 or self.rect.left>500 or self.rect.right < 0 or self.rect.bottom<0:
            self.kill()
        if (self.speedy >-3 and self.speedy<3) or (self.speedx>-3 and self.speedx<3):
            self.kill()
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(4):
    reborn()
triggerx = False
triggery = False
detriggerx = False
detriggery = False

font_name = os.path.join("Running_Script.ttf")
def draw_text(surf,text,size,x,y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text, True,'white')
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface,text_rect)
def draw_health(surf,hp,x,y):
    if hp<0:
        hp=0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill =(hp/100)*BAR_LENGTH
    outline_rect = pygame.Rect(x,y,BAR_LENGTH,BAR_HEIGHT)
    fill_rect = pygame.Rect(x,y,fill,BAR_HEIGHT)
    pygame.draw.rect(surf,'green',fill_rect)
    pygame.draw.rect(surf,'white',outline_rect,2)
def draw_init():
    screen.fill((0,0,0))
    draw_text(screen,'謝謝遊玩，你的分數為:', 32,250,150)
    draw_text(screen,str(score),64,250,250)
    draw_text(screen,'作者：吳宇藤',22,250,400)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


upgrade = False
grade = 0
power =1000

while running:
    clock.tick(fps)
    ret, img = cap.read()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    img = cv.resize(img,(0,0),fx=0.5,fy=0.5)
    if ret:
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        result = hands.process(imgRGB)
        imgHeight = img.shape[0]
        imgWidth = img.shape[1]
        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                mpDraw.draw_landmarks(img,handLms,mphands.HAND_CONNECTIONS,handStylems,handStylecon)
                for i,lm in enumerate(handLms.landmark): #i表示第幾個點
                    xPos = int(lm.x*imgWidth)
                    yPos = int(lm.y*imgHeight)
                    
                    #print(i,xPos,yPos)
                    
                    if i == 8:
                        
                        cv.circle(img,(xPos,yPos),20,(166,25,23),cv.FILLED)
                        if xPos <=150:
                            triggerx = True
                        elif xPos>=500:
                            detriggerx = True
                        else:
                            triggerx = False
                            detriggerx = False
                        if yPos <=150:
                            triggery = True
                        elif yPos >= 250:
                            detriggery = True
                        else:
                            triggery = False
                            detriggery = False
        else:       
            triggerx = False
            triggery = False
            detriggerx = False
            detriggery = False         
              
        cv.imshow('img',img)
    
    if cv.waitKey(1)== ord('q'):
        break
    #print(img.shape[0],img.shape[1])
    for i in range(14):
        player.shoot()
    all_sprites.update()
    hits=pygame.sprite.groupcollide(enemies,bullets,True,True)
    for hit in hits:
        score+=100
        solo_reborn()
    hits = pygame.sprite.spritecollide(player,enemies,True)
    for hit in hits:
        player.health -= 20
        if player.health <=0:
            running = False  
            solo_reborn()
    
    if score -grade>=power:
        upgrade = True
        if upgrade == True:
            for i in range(2):
                reborn()
        grade = score
        power *=2
        upgrade = False
    if player.health<= 0:
        draw_init()
            
        
    screen.fill('black')
    all_sprites.draw(screen)
    draw_text(screen,str(score),20,250,10)
    draw_health(screen,player.health,player.rect.x-25,player.rect.y-15)
    pygame.display.update()
pygame.quit()