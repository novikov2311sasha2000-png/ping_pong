from pygame import *
import gif_pygame
from random import randint

font.init()
font = font.SysFont('Arial', 100)
right_win = font.render('Right WIN!', True, (255, 215, 0))
left_win = font.render('Left WIN!', True, (255, 0, 0))

window = display.set_mode((1500, 700)) # set_mode - устанавливает размеры окна
display.set_caption('Ping-pong') # set_caption - устанавливает название окна
background = transform.scale(image.load('white.png'), (1500, 700)) # scale - подгоняет размеры картинки под нужные

# mixer.init()
# mixer.music.load('Cu.ogg') # загрузка файла с музыкой
# mixer.music.set_volume(0.1) # set_volume - делает звук тише (1 - максимум)
# mixer.music.play(0) # play - проигрывает звук
# kick = mixer.Sound('Cu.ogg')

clock = time.Clock() # Clock - класс для создания таймера
FPS = 60
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_w, player_h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect() # get_rect - создаёт прямоугольник
        self.rect.x = player_x
        self.rect.y = player_y
        self.player_w = player_w
        self.player_h = player_h
    
    def up_object(self):
        self.rect.y -= 5

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update(self, up, down):
        keys_pressed = key.get_pressed() # get_pressed - возвращает все нажатые клавиши
        if keys_pressed[up] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[down] and self.rect.y < 420:
            self.rect.y += self.speed    
        if not keys_pressed[up] and not keys_pressed[down]:
            pass

fake_player = gif_pygame.load('ping.png')
player = Player('Rect.png', 250, 250, 45, 275, 5)

fake_player_2 = gif_pygame.load('ping.png')
player_2 = Player('Rect.png', 1100, 250, 45, 275, 5)

fake_pong = gif_pygame.load('pong.png')
pong = GameSprite('Rect.png', 850, 250, 54, 58, 5)
speed_1 = 5
speed_2 = 5

fini = False
game = True
while game:

    for i in event.get():
        if i.type == QUIT: 
            game = False
    if fini != True:
        window.blit(background, (0, 0))

        player.update(K_w, K_s)
        player.reset()
        fake_player.render(window, (player.rect.x, player.rect.y))

        player_2.update(K_UP, K_DOWN)
        player_2.reset()
        fake_player_2.render(window, (player_2.rect.x, player_2.rect.y))

        pong.reset()
        fake_pong.render(window, (pong.rect.x, pong.rect.y))
        pong.rect.x += speed_1
        pong.rect.y += speed_2
        if pong.rect.colliderect(player.rect) or pong.rect.colliderect(player_2.rect):
            speed_1 *= -1
            if randint(1, 2) == 1:
                speed_2 *= -1
        if pong.rect.y <= 0 or pong.rect.y >= 650:
            speed_2 *= -1

        if pong.rect.x < 150:
            window.blit(left_win, (500, 250))
            fini = True
        elif pong.rect.x > 1350:
            window.blit(right_win, (500, 250))
            fini = True

    display.update() 
    clock.tick(FPS) 
