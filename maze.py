from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,  player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        display1.blit(self.image, (self.rect.x, self.rect.y))

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, width, height, wall_x, wall_y):
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        display1.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed


class Enemy(GameSprite):
    directional = 'left'
    def update(self):
        if self.rect.x < 450:
            self.directional = 'right'
        if self.rect.x > 615:
            self.directional = 'left'

        if self.directional == 'left':
            self.rect.x -= self.speed
        if self.directional == 'right':
            self.rect.x += self.speed


display1 = display.set_mode((700, 500))
display.set_caption('Maze')

background = transform.scale(image.load('background.jpg'), (700, 500))
player1 = Player('hero.png', 5, 420, 3)
enemy = Enemy('cyborg.png', 620, 280, 4)
enemy1 = Enemy('pudj.png', 620, 220, 2)
treasure = GameSprite('treasure.png', 620, 20, 0)
wall1 = Wall(110, 11, 34, 20, 350, 160, 150)
wall2 = Wall(110, 11, 34, 50, 20, 180, 150)
wall3 = Wall(110, 11, 34, 20, 350, 230, 150)
wall4 = Wall(110, 11, 34, 20, 350, 350, 0)
wall5 = Wall(110, 11, 34, 50, 20, 370, 330)
wall6 = Wall(110, 11, 34, 20, 350, 420, 0)



mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

game = True
finish = False
fps = 60
game_cycle = time.Clock()

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))


while game:
    for every in event.get():
        if every.type == QUIT:
            game = False

    if finish != True:
        display1.blit(background, (0, 0))
        player1.update()
        player1.reset()
        enemy.update()
        enemy.reset()
        enemy1.update()
        enemy1.reset()
        treasure.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()

        if sprite.collide_rect(player1, enemy) or sprite.collide_rect(player1, enemy1) or sprite.collide_rect(player1, wall1) or sprite.collide_rect(player1, wall2) or sprite.collide_rect(player1, wall3) or sprite.collide_rect(player1, wall4) or sprite.collide_rect(player1, wall5) or sprite.collide_rect(player1, wall6):
            finish = True
            display1.blit(lose, (200, 200))
            kick.play()
        elif sprite.collide_rect(player1, treasure):
            finish = True
            display1.blit(win, (200, 200))
            money.play()
    display.update()
    game_cycle.tick(fps)