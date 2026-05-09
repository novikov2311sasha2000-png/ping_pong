from pygame import *

font.init()
font = font.SysFont('Arial', 100)
right_win = font.render('Right WIN!', True, (255, 215, 0))
left_win = font.render('Left WIN!', True, (255, 0, 0))

window = display.set_mode((1500, 700)) # set_mode - устанавливает размеры окна
display.set_caption('Догонялки') # set_caption - устанавливает название окна
background = transform.scale(image.load('white.png'), (1500, 700)) # scale - подгоняет размеры картинки под нужные
#создай 2 спрайта и размести их на сцене

# player = transform.scale(image.load('Bug_pikcher.png'), (100, 100))

# mixer.init()
# mixer.music.load('forest.mp3') # загрузка файла с музыкой
# mixer.music.set_volume(0.1) # set_volume - делает звук тише (1 - максимум)
# mixer.music.play(0) # play - проигрывает звук
# kick = mixer.Sound('kick.ogg')


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
    def update(self):
        keys_pressed = key.get_pressed() # get_pressed - возвращает все нажатые клавиши
        if keys_pressed[K_a] and keys_pressed[K_w] and self.rect.x > 5 and self.rect.y > 5:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
            png_1 = 'NW_B1.png'
        elif keys_pressed[K_a] and keys_pressed[K_s] and self.rect.x > 5 and self.rect.y < 625:
            self.rect.x -= self.speed
            self.rect.y += self.speed
            png_1 = 'SW_B1.png'
        elif keys_pressed[K_d] and keys_pressed[K_s] and self.rect.x < 1400 and self.rect.y < 625:
            self.rect.x += self.speed
            self.rect.y += self.speed
            png_1 = 'SE_B1.png'
        elif keys_pressed[K_d] and keys_pressed[K_w] and self.rect.x < 1400 and self.rect.y > 5:
            self.rect.x += self.speed
            self.rect.y -= self.speed
            png_1 = 'NE_B1.png'
        elif keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
            png_1 = 'W_B1.png'
        elif keys_pressed[K_d] and self.rect.x < 1400:
            self.rect.x += self.speed
            png_1 = 'E_B1.png'
        elif keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
            png_1 = 'N_B1.png'
        elif keys_pressed[K_s] and self.rect.y < 625:
            self.rect.y += self.speed   
            png_1 = 'S_B1.png' 
        elif not keys_pressed[K_s] and not keys_pressed[K_a] and not keys_pressed[K_d] and not keys_pressed[K_w]:
            png_1 = 'B1.png'
        return png_1 
        
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 1000:
            self.direction = 'right'
        if self.rect.x >= 1500 - 125:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'right':
            self.rect.x += self.speed
    def update_2(self):
        if self.rect.y <= 0:
            self.direction = 'down'
        if self.rect.y >= 675 - 125:
            self.direction = 'up'
        if self.direction == 'down':
            self.rect.y += self.speed
        elif self.direction == 'up':
            self.rect.y -= self.speed
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_w, wall_h):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wall_w = wall_w
        self.wall_h = wall_h
        self.image = Surface((self.wall_w, self.wall_h)) # Surface - создаёт картинку-прямоугольник определённой высоты и ширины
        self.image.fill((color_1, color_2, color_3)) # fill - заливка
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y   
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def up_object(self):
        self.rect.y -= 5
        # временный мотод


fini = False
game = True
while game:

    for i in event.get():
        if i.type == QUIT: # < если событие = нажат крест
            game = False
    if fini != True:
        window.blit(background, (0, 0))
             
    display.update() # update - обновляет экран
    clock.tick(FPS) # tick - задаёт кол-во раз срабатываий while в секунду