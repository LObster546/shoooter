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
        bullet = Bullet('bullet.png', 30, 20, self.rect.centerx, self.rect.centery, 10)
        bullets.add(bullet)


class Bullet(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < -2:
            self.kill()

#фон
window = display.set_mode((1000, 700))
display.set_caption('Шутер')
background1 = transform.scale(image.load('loc0.png'), (1000, 700))

background2 = transform.scale(image.load('loc1.png'), (1000, 700))

background3 = transform.scale(image.load('loc1.png'), (1000, 700))

#спрайты
s_hero = PLayer('pixil-frame-0.png', 300, 350, 480, 600, 7)

bullets = sprite.Group()















clock = time.Clock()
FPS = 50



finish = False
game = True
while game:
    if not finish:

        #команты
        if room == 0:
            window.blit(background1, (0, 0))


        if s_hero.rect.x < -2:
            room += 1
            s_hero.rect.x = 900
            s_hero.rect.y = 600


        if room == 1:
            window.blit(background2, (0, 0))

        if room == 2:
            window.blit(background3, (0, 0))


        #
        s_hero.update()
        s_hero.reset()

        bullets.update()
        bullets.draw(window)






    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                s_hero.fire()
        if e.type == MOUSEMOTION :
            pass










    display.update()
    clock.tick(FPS)
