
import pygame as pg
import os
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
size = WIDTH, HEIGHT = (840, 480)


def drawLineBetween(screen, start, end, rad, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pg.draw.circle(screen, color, (x, y), rad)


colors = ['red', 'yellow', 'blue', 'orange', 'green', 'black']


def main():
    pg.init()
    text = pg.font.SysFont('comicans', 30)
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    pg.display.set_caption('PAINT')
    screen = pg.display.set_mode(size)
    screen.fill(WHITE)
    clock = pg.time.Clock()
    color = 'black'
    done = True
    shape = False
    mode = 1
    radius = 1
    panel = pg.Surface((50, HEIGHT))
    panel.fill(WHITE)
    pg.draw.rect(panel, BLACK, (0, 0, 50, HEIGHT), 1)
    panel.blit(pg.transform.scale(pg.image.load(
        'pen_image.png'), (40, 40)), (5, 10))
    panel.blit(pg.transform.scale(pg.image.load(
        'eraser_image.png'), (40, 40)), (5, 60))
    pg.draw.rect(panel, BLACK, (5, 110, 40, 40), 2)
    pg.draw.circle(panel, BLACK, (25, 180), 20, 2)
    for i in range(len(colors)):
        pg.draw.rect(panel, pg.Color(colors[i]), (10, 220+i*30, 20, 20))
    screen.blit(panel, (0, 0))
    area_to_save = None
    points = []

    while True:
        pressed_key = pg.key.get_pressed()
        for event in pg.event.get():
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_KP_PLUS:
                    radius = min(200, radius + 1)
                if event.key == pg.K_KP_MINUS:
                    radius = max(1, radius - 1)
                if event.key == pg.K_c:
                    pg.draw.rect(screen, WHITE, (50, 0, WIDTH, HEIGHT))
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return
            if event.type == pg.MOUSEBUTTONUP:
                points = []
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if 5 < event.pos[0] < 45:
                    if 10 < event.pos[1] < 50:
                        mode = 1
                        radius = 1
                    elif 60 < event.pos[1] < 100:
                        mode = 3
                        radius = 5
                        color = 'white'
                    elif 110 < event.pos[1] < 160:
                        mode = 2
                        shape = False
                    elif 170 < event.pos[1] < 220:
                        mode = 2
                        shape = True
                    elif 220 < event.pos[1] < 250:
                        color = 'red'
                    elif 250 < event.pos[1] < 280:
                        color = 'yellow'
                    elif 280 < event.pos[1] < 310:
                        color = 'blue'
                    elif 310 < event.pos[1] < 340:
                        color = 'orange'
                    elif 340 < event.pos[1] < 370:
                        color = 'green'
                    elif 370 < event.pos[1] < 400:
                        color = 'black'
                if mode != 3 and color == 'white':
                    radius = 1
                    color = 'black'
                if mode == 2:
                    done = False
                    x1, y1 = event.pos
                    area_to_save = screen.copy()
                else:
                    if (50+radius, 0) < event.pos < size:
                        pg.draw.circle(screen, pg.Color(
                            color), event.pos, radius)
                        points += [event.pos]
            if event.type == pg.MOUSEMOTION and (50+radius, 0) < event.pos < size and pg.mouse.get_pressed()[0]:
                # if mouse moved, add point to list
                if mode != 2:
                    points += [event.pos]
                elif not done:
                    x2, y2 = event.pos
                    width, height = abs(x1-x2), abs(y1-y2)
                    screen.blit(area_to_save, (0, 0))
                    if shape:
                        pg.draw.ellipse(screen, pg.Color(
                            color), (x1 - width*(x2 < x1), y1 - height*(y2 < y1), width, height), radius)
                    else:
                        pg.draw.rect(screen, pg.Color(
                            color), (x1 - width*(x2 < x1), y1 - height*(y2 < y1), width, height), radius)

        if mode != 2:
            i = 0
            while i < len(points) - 1:
                drawLineBetween(
                    screen, points[i], points[i + 1], radius, color)
                i += 1
        pg.draw.rect(screen, WHITE, (2, HEIGHT-20, 47, 30))
        screen.blit(text.render(f'S:{radius}', True, BLACK), (2, HEIGHT-20))
        pg.display.flip()

        clock.tick(FPS)


main()

