import pygame as pg
import sys

# setup
pg.init()
clock = pg.time.Clock()

# setting up the window
width = 1280
height = 920
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Pong")

ball = pg.Rect(width/2 - 15, height/2 - 15, 30, 30)
player = pg.Rect(width - 20, height/2 - 70, 10, 140)
opponent = pg.Rect(10, height/2 - 70, 10, 140)

# adding color
screen.fill(pg.Color('Silver'))
pg.draw.ellipse(screen, pg.Color('Black'), ball)
pg.draw.rect(screen, pg.Color('Grey9'), player)
pg.draw.rect(screen, pg.Color('Grey9'), opponent)
pg.draw.aaline(screen, pg.Color('Grey9'), (width/2, 0), (width/2, height))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.flip()
    clock.tick(60)