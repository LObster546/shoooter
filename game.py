
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
boss_h = 5
shoot_h = 1

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
            if not (sprite.collide_rect(s_hero, wallw3) or sprite.collide_rect(s_hero, wallw3_2) or sprite.collide_rect(s_hero, l1wall1) or sprite.collide_rect(s_hero, l1wall2) or sprite.collide_rect(s_hero, l2wall1) or sprite.collide_rect(s_hero, l3wall1) or sprite.collide_rect(s_hero, l3wall2) or sprite.collide_rect(s_hero, l2wall2) or sprite.collide_rect(s_hero, l2_door)):
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
        bullet = Bullet('bullet.png', 15, 10, self.rect.centerx, self.rect.centery, 10)
        bullets.add(bullet)

    



        

class MeleeEnemy(GameSprite):
    direction = 'down'
    def update(self):
        if (sprite.collide_rect(s_l1menemy1, wallw1) or sprite.collide_rect(s_l2menemy1, wallw1) or sprite.collide_rect(s_l2menemy1, l2wall2)):
            self.direction = 'down'
        if sprite.collide_rect(s_l1menemy1, wallw2):
            self.direction = 'up'
        
        if self.direction == 'up':
            self.rect.y -= self.speed
        if self.direction == 'down':
            self.rect.y += self.speed



class BossEnemy(GameSprite):
    direction_B = 'down'
    def update(self):
        if sprite.collide_rect(s_boss, wallw1):
            self.direction_B = 'down'
        if sprite.collide_rect(s_boss, wallw2):
            self.direction_B = 'up'
        
        if self.direction_B == 'up':
            self.rect.y -= self.speed
        if self.direction_B == 'down':
            self.rect.y += self.speed


    def bossfire(self):
        enemybullet = EnemyBullet('enemybullet.png',20, 15, self.rect.centerx, self.rect.centery, 7)
        
        enbullets.add(enemybullet)
        



class ShootEnemy(GameSprite):
    #def update(self):


    def enemyfire(self):
        enemybullet = EnemyBullet('enemybullet.png',20, 15, self.rect.centerx, self.rect.centery, 7)
        
        enbullets.add(enemybullet)




class Bullet(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        sprite.groupcollide(bullets, walls, True, False)
        

        if self.rect.x < -2:
            self.kill()

class EnemyBullet(GameSprite):
    def update(self):
        self.rect.x += self.speed
        sprite.groupcollide(enbullets, walls, True, False)


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

s_l1menemy1 = MeleeEnemy('enemy2.png', 100, 100, 500, 100, 4)
s_l1menemy2 = MeleeEnemy('enemy2.png', 100, 100, 100, 300, 0)

s_l2menemy1 = MeleeEnemy('enemy2.png', 100, 100, 100, 700, 4)

s_l2menemy2 = MeleeEnemy('enemy2.png', 100, 100, 100, 50, 4)

s_l2shoot_enemy1 = ShootEnemy('enemy1.png', 150, 100, 10, 10, 0)

s_boss = BossEnemy('boss.png', 200, 150, 200, 300, 3)

'''пули'''
bullets = sprite.Group()
enbullets = sprite.Group()



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
l3wall2 = Wall(60, 60, 60, l3w2_x, l3w2_y, 20, 500)

#кнопка
l2_bd = GameSprite('button0.png', 100, 100, 5, 50, 0)


#двери
l2_door = Wall(255, 0, 0, 10000, 250, 10, 300)

hp_bar = GameSprite('BossHP5.png', 400, 50, 300, 10, 0)

'''БОЧКИ'''
#1 лока
l1_bar1 = GameSprite('barell1.png', 60, 65, 10, 40, 0) 
l1_bar2 = GameSprite('barell3.png', 120, 120, 140, 10, 0)
l1_bar3 = GameSprite('barell1.png', 60, 65, 10, 600, 0)

#2 лока
l2_bar1 = GameSprite('barell1.png', 60, 65, 10, 200, 0)
l2_bar2 = GameSprite('barell3.png', 120, 120, 10, 550, 0)
#3 лока
l3_bar1 = GameSprite('barell2.png', 100, 90, 10, 600, 0)
l3_bar2 = GameSprite('barell3.png', 120, 120, 520, 550, 0)

mixer.init()




b = 0


clock = time.Clock()
FPS = 50

button = sprite.Group(l2_bd)
endwall = sprite.Group(l3wall1)
walls = sprite.Group(wallw1, wallw2, wallw3, wallw3_2, wallw4, l1wall1, l1wall2, l2wall1, l2wall2, l3wall2)
menemy = sprite.Group(s_l1menemy1, s_l1menemy2, s_l2menemy1, s_l2menemy2)
senemy = sprite.Group(s_l2shoot_enemy1)
hero = sprite.Group(s_hero)
bosses = sprite.Group(s_boss)

walls.add()

font.init()
font = font.Font(None, 70)
win = font.render('Победа', True, (255, 255 , 0))
lose = font.render('Ты умер ', True, (255, 0, 0))

finish = False
game = True


shootInterval = 50
shootTimer = 0

bossInterval = 25
bossTimer = 0

while game:
    if not finish:
        wallw1.draw_wall()
        wallw2.draw_wall()
        wallw4.draw_wall()
        sprite.groupcollide(bullets, menemy, True, True)



        if sprite.groupcollide(bullets, senemy, True, True):
            shoot_h += 1

        
            

        #команты
        if room == 0:
            window.blit(background1, (0, 0))

            l1wall1.draw_wall()
            l1wall2.draw_wall()

            l1_bar1.update()
            l1_bar1.reset()

            l1_bar2.update()
            l1_bar2.reset()

            l1_bar3.update()
            l1_bar3.reset()

            
            s_l2menemy2.rect.x = 10000
            s_l2menemy1.rect.x = 10000
            
            s_l2shoot_enemy1.rect.x = 10000



        if s_hero.rect.x < -100:
            room += 1
            s_hero.rect.x = 900
            s_hero.rect.y = 300


        if room == 1:
            l1wall1.rect.x = 10000
            l1wall1.rect.y = 10000
            l1wall2.rect.x = 10000
            l1wall2.rect.y = 10000


            s_l2shoot_enemy1.rect.x = 200
            s_l2shoot_enemy1.rect.y = 150

            s_l2menemy2.rect.x = 50
            s_l2menemy2.rect.y = 300



            l2wall1.rect.x = 800
            l2wall1.rect.y = 300

            l2wall2.rect.x = 1
            l2wall2.rect.y = 270
            window.blit(background2, (0, 0))

            l2_door.draw_wall()
            if b == 0:
                l2_door.rect.x = 1

            l2wall1.draw_wall()
            l2wall2.draw_wall()

            l2_bd.update()
            l2_bd.reset()

            l2_bar1.update()
            l2_bar1.reset()

            l2_bar2.update()
            l2_bar2.reset()

            

            s_l1menemy1.kill()
            s_l1menemy2.kill()



            s_l2menemy1.rect.y = 100
            s_l2menemy1.rect.x = 500

        if room == 2:
            if sprite.groupcollide(bullets, bosses, True, False):
                boss_h -= 1
                if boss_h <= 0:
                    s_boss.kill()


            window.blit(background3, (0, 0))
            l2wall1.rect.x = 10000
            l2wall1.rect.y = 10000
            l2wall2.rect.x = 10000
            l2wall2.rect.y = 10000

            s_l2menemy1.kill()
            s_l2shoot_enemy1.kill()
            s_l2menemy2.kill()

            shoot_h = 2

            l3_bar1.update()
            l3_bar1.reset()

            l3_bar2.update()
            l3_bar2.reset()

            hp_bar.update()
            hp_bar.reset()

            l1_bar1.update()
            l1_bar1.reset()

            bosses.update()
            bosses.draw(window)
            
            l3wall1.rect.x = 0
            l3wall1.rect.y = 250

            l3wall2.rect.x = 500
            l3wall2.rect.y = 400

            l3wall1.draw_wall()
            l3wall2.draw_wall()
            s_l1menemy1.kill()
            s_l1menemy2.kill()


        

        #
        s_hero.update()
        s_hero.reset()


        


        wallw3.draw_wall()
        wallw3_2.draw_wall()

        senemy.update()
        senemy.draw(window)

        menemy.update()
        menemy.draw(window)


        bullets.update()
        bullets.draw(window)
        if boss_h == 4:
            hp_bar = GameSprite('BossHP4.png', 400, 50, 300, 10, 0)
        if boss_h == 3:
            hp_bar = GameSprite('BossHP3.png', 400, 50, 300, 10, 0)
        if boss_h == 2:
            hp_bar = GameSprite('BossHP2.png', 400, 50, 300, 10, 0)
        if boss_h == 1:
            hp_bar = GameSprite('BossHP1.png', 400, 50, 300, 10, 0)
        if boss_h == 0:
            hp_bar = GameSprite('BossHP0.png', 400, 50, 300, 10, 0)




        if not shoot_h > 1 :
            if s_l2shoot_enemy1.rect.y - 100 <= s_hero.rect.y <= s_l2shoot_enemy1.rect.y + 100:
                if shootTimer == 0:
                    s_l2shoot_enemy1.enemyfire()
                    shootTimer = shootInterval
                shootTimer -= 1
                    

        if boss_h > 0 and room == 2:
            if s_boss.rect.y - 100 <= s_hero.rect.y <= s_boss.rect.y + 100:
                if bossTimer == 0:
                    s_boss.bossfire()
                    bossTimer = bossInterval
                bossTimer -= 1
                
            

        enbullets.update()
        enbullets.draw(window)  

        if sprite.groupcollide(hero, button, False, False):
            l2_bd = GameSprite('button1.png', 100, 100, 5, 50, 0)
            l2_door.kill()
            l2_door.rect.x = 10000
            b += 1

        if sprite.groupcollide(enbullets, hero, True, True) or sprite.groupcollide(hero, menemy, True, False):
            finish = True
            window.blit(lose, (300, 300))

        if boss_h == 0:
            if sprite.groupcollide(hero, endwall , False, False):
                finish = True
                window.blit(win, (300, 300))





    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                s_hero.fire()
        


    display.update()
    clock.tick(FPS)
