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
           
            self.rect.x -= self.speed
        if keys_pressed[K_d]:
            self.rect.x += self.speed
            
        if keys_pressed[K_s]:
            self.rect.y += self.speed
      
        if keys_pressed[K_w]:
            self.rect.y -= self.speed
 


    def fire(self):
        bullet = Bullet('bullet.png', 20, 15, self.rect.centerx, self.rect.centery, 10)
        bullets.add(bullet)

    def enemyfire():
        pass

class MeleeEnemy(GameSprite):
    pass
class Bullet(GameSprite):
    def update(self):
        self.rect.x -= self.speed
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
s_hero = PLayer('player.png', 300, 350, 800, 300, 7)

bullets = sprite.Group()
#гл стены 
wallw1 = Wall(255, 0, 0, -3, 0, 1500, 1)
wallw2 = Wall(255, 0, 0, 705, 0, 1500, 1)
wallw3 = Wall(255, 0, 0, 0, -10, 5, 300)
wallw3_2 = Wall(255, 0, 0, 0, 500, 5, 300)
wallw4 = Wall(255, 0, 0, -3, 1001, 1, 750)

#стены 1 локации
l1wall1 = Wall(255, 0, 0, 430, -10, 10, 300)
l1wall2 = Wall(255, 0, 0, 430, 550, 10, 300)
#стены 2 локации
l2wall1 = Wall(255, 0, 0, 700, 500, 300, 10)

#стены 3 локации\




#двери

#кнопка







mixer.init()







clock = time.Clock()
FPS = 50

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
            window.blit(background2, (0, 0))

            l2wall1.draw_wall()

        if room == 2:
            window.blit(background3, (0, 0))


        #
        s_hero.update()
        s_hero.reset()
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
