import pygame as pg
import datetime
pg.init()
WIDTH = 800
HEIGHT = 600
FPS = 60
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Clock')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
background = pg.transform.scale(pg.image.load('/Users/elsanarsen/Desktop/pp2022/week 7/Main.jpeg'), (WIDTH, HEIGHT))
pg.mixer.music.load('/Users/elsanarsen/Desktop/pp2022/week/background.wav')
pg.mixer.music.play(-1)

font = pg.font.SysFont("Times New Roman", 30)


right = pg.image.load('/Users/elsanarsen/Desktop/pp2022/week 7/HourHand.png')
left = pg.image.load('/Users/elsanarsen/Desktop/pp2022/week 7/MinHand.png')
# Changing resolution
# 1400//1,75 = 800 and 1050//1,75 = 600 then 1450x1050 => 800x600
rhand = pg.transform.scale(pg.image.load('/Users/elsanarsen/Desktop/pp2022/week 7/HourHand.png'), (right.get_width()//1.75, right.get_height()//1.75))
lhand = pg.transform.scale(pg.image.load('/Users/elsanarsen/Desktop/pp2022/week 7/MInHand.png'), (left.get_width()//1.75, left.get_height()//1.75))

def blit_rotate_center(image, x0, y0, angel):  # topleft x0 and y0 coordinates of the image
    rotated_image = pg.transform.rotate(image, angel)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=(x0, y0)).center)
    screen.blit(rotated_image, new_rect)


running = True
while running:
    clock.tick(FPS)
    screen.blit(background, (0, 0))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    time = datetime.datetime.now()
    hour = time.hour
    minute = time.minute
    second = time.second
    
    screen.blit(background, (0, 0))
    text = font.render(f'The time is now: {hour}:{minute}:{second}', True, BLUE)
    # blit_rotate_center(rhand, WIDTH // 2 - rhand.get_width()//2, HEIGHT // 2 - rhand.get_height()//2,
    #                    (-6*hour) + 105)  # Error 105
    blit_rotate_center(rhand, WIDTH // 2 - rhand.get_width()//2, HEIGHT // 2 - rhand.get_height()//2,
                       (-6*(minute+second/60)) - 11)  # Error 11
    blit_rotate_center(lhand, WIDTH // 2 - lhand.get_width() // 2, HEIGHT // 2 - lhand.get_height() // 2,
                       (-6*second) - 3)  # Error 3
    screen.blit(text, (250, 550))

    pg.display.update()
pg.quit()
exit()

