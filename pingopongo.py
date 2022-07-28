from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x,player_y,
    player_width,player_height ,player_speed):
        super().__init__()
        self.image = transform.scale(
            image.load(player_image),(player_width,player_height)
            )
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
window.fill((200,255,255))
clock = time.Clock()
display.set_caption("PingPong")
FPS = 60
game = True
finish = False

racket1 = Player('racket.png', 5, win_height / 2, 30, 100, 10)
racket2 = Player('racket.png', win_width-30, win_height / 2, 30, 100, 10)

while game:
    if not finish:
        racket1.reset()
        racket2.reset()
        racket1.update_l()
        racket2.update_r()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)

