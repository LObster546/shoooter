
from typing import Any
from pygame import*
from random import *
import math  
#Игра
# шутер цель которого добраться до конца отстреливаясь от врагов и решая иногда 
# простые головолмки и прочие мини игры
#будет примерно 3 локации через которые можно будет почти  свободно передвигаться
#Управление: w a s d - хотьба,  ЛКМ - стрельба
#У игрока только 1 жизнь, по пути будут встречаться: двигующиеся враги, стреляющие, стоящие(наверное)

room = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_w, player_h, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h)) #100 60
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class PLayer(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        

        if keys_pressed[K_a]:
            if not (sprite.collide_rect(s_hero, wallw3) or sprite.collide_rect(s_hero, wallw3_2) or sprite.collide_rect(s_hero, l1wall1) or sprite.collide_rect(s_hero, l1wall2) or sprite.collide_rect(s_hero, l2wall1) or sprite.collide_rect(s_hero, l3wall1) or sprite.collide_rect(s_hero, l3wall2) or sprite.collide_rect(s_hero, l2wall2)):
                self.rect.x -= self.speed
        if keys_pressed[K_d]:
            if not (sprite.collide_rect(s_hero, wallw4) or sprite.collide_rect(s_hero, l1wall1) or sprite.collide_rect(s_hero, l1wall2) or sprite.collide_rect(s_hero, l2wall1) or sprite.collide_rect(s_hero, l3wall2)) :
                self.rect.x += self.speed
            
        if keys_pressed[K_s]:
            if not (sprite.collide_rect(s_hero, wallw2) or sprite.collide_rect(s_hero, l2wall2)):
                self.rect.y += self.speed
    
        if keys_pressed[K_w]:
            if not sprite.collide_rect(s_hero, wallw1):
                self.rect.y -= self.speed
 


    def fire(self):
        bullet = Bullet('bullet.png', 20, 15, self.rect.centerx, self.rect.centery, 10)
        bullets.add(bullet)

    def enemyfire():



        pass

class MeleeEnemy_lr(GameSprite):
    direction = 'left'
    def update(self):
        if sprite.collide_rect(s_menemy, wallw3):
            self.direction = 'right'
        if sprite.collide_rect(s_menemy, l1wall1):
            self.direction = 'left'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed




class Bullet(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        sprite.groupcollide(bullets, walls, True, False)

        if self.rect.x < -2:
            self.kill()
class Wall(sprite.Sprite):
    def __init__(self, r, g, b, x, y, w, h):
        super().__init__()
        self.red = r
        self.green = g
        self.blue = b

        self.width = w
        self.height = h
        self.image = Surface((self.width, self.height))
        self.image.fill((r, g, b))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Door(sprite.Sprite):
    def __init__(self, r, g, b, x, y, w, h):
        super().__init__()
        self.red = r
        self.green = g
        self.blue = b

        self.width = w
        self.height = h
        self.image = Surface((self.width, self.height))
        self.image.fill((r, g, b))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



    def draw_door(self):
        window.blit(self.image, (self.rect.x, self.rect.y))





#фон
window = display.set_mode((1000, 700))
display.set_caption('Шутер')
background1 = transform.scale(image.load('loc0.png'), (1000, 700))

background2 = transform.scale(image.load('loc1.png'), (1000, 700))

background3 = transform.scale(image.load('loc1.png'), (1000, 700))

#спрайты
s_hero = PLayer('player.png', 100, 100, 800, 300, 7)

s_menemy = MeleeEnemy_lr('enemy2.png', 100, 100, 50, 100, 4)

bullets = sprite.Group()



#гл стены 
wallw1 = Wall(60, 60, 60, -3, 0, 1500, 1) #верхняя сена мира
wallw2 = Wall(60, 60, 60, -3, 703, 1500, 1) #нижняя стена мира
wallw3 = Wall(60, 60, 60, 0, -10, 10, 300) 
wallw3_2 = Wall(60, 60, 60, 0, 500, 10, 300)
wallw4 = Wall(60, 0, 0, 1001, 0, 1, 750) #правая сnена мира

#стены 1 локации
'''корды стен'''
l1w1_x = 430
l1w1_y = -10
l1w2_x = 430
l1w2_y = 550

l1wall1 = Wall(60, 60, 60, l1w1_x, l1w1_y, 20, 300)
l1wall2 = Wall(60, 60, 60, 430, 550, 20, 300)
#стены 2 локации
l2w1_x = 10000
l2w1_y = 10000

l2w2_x = 10000
l2w2_y = 10000
#800 300
#1 270
l2wall1 = Wall(60, 60, 60, l2w1_x, l2w1_y, 10, 500)
l2wall2 = Wall(60, 60, 60, l2w2_x, l2w2_y, 500, 10)

#стены 3 локации\
l3w1_x = 10000
l3w1_y = 10000

l3w2_x = 10000
l3w2_y = 10000

#0 250
#500 400
l3wall1 = Wall(0, 255, 0, l3w1_x, l3w1_y, 5, 300)
l3wall2 = Wall(60, 60, 60, l3w2_x, l3w2_y, 10, 500)




#двери

#кнопка







mixer.init()







clock = time.Clock()
FPS = 50

walls = sprite.Group(wallw1, wallw2, wallw3, wallw3_2, wallw4, l1wall1, l1wall2, l2wall1, l2wall2, l3wall1, l3wall2)
walls.add()

font.init()
font = font.Font(None, 70)
win = font.render('Победа', True, (255, 0, 0))
lose = font.render('Проигрыш ', True, (255, 0, 0))

finish = False
game = True
while game:
    if not finish:
        wallw1.draw_wall()
        wallw2.draw_wall()
        wallw4.draw_wall()


        #команты
        if room == 0:
            window.blit(background1, (0, 0))

            l1wall1.draw_wall()
            l1wall2.draw_wall()


        if s_hero.rect.x < -100:
            room += 1
            s_hero.rect.x = 900
            s_hero.rect.y = 300


        if room == 1:
            l1wall1.rect.x = 10000
            l1wall1.rect.y = 10000
            l1wall2.rect.x = 10000
            l1wall2.rect.y = 10000



            l2wall1.rect.x = 800
            l2wall1.rect.y = 300

            l2wall2.rect.x = 1
            l2wall2.rect.y = 270
            window.blit(background2, (0, 0))

            l2wall1.draw_wall()
            l2wall2.draw_wall()

        if room == 2:
            window.blit(background3, (0, 0))
            l2wall1.rect.x = 10000
            l2wall1.rect.y = 10000
            l2wall2.rect.x = 10000
            l2wall2.rect.y = 10000

            l3wall1.rect.x = 0
            l3wall1.rect.y = 250

            l3wall2.rect.x = 500
            l3wall2.rect.y = 400

            l3wall1.draw_wall()
            l3wall2.draw_wall()


        

        #
        s_hero.update()
        s_hero.reset()

        s_menemy.update()
        s_menemy.reset()


        wallw3.draw_wall()
        wallw3_2.draw_wall()











        bullets.update()
        bullets.draw(window)







    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                s_hero.fire()



















    display.update()
    clock.tick(FPS)
