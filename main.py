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

def ball_animation():
    global ball_speed_x, ball_speed_y
    # sets speed to the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #collisions
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= width:
        ball_speed_x *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

# shape and its dimentions
ball = pg.Rect(width/2 - 15, height/2 - 15, 30, 30)
player = pg.Rect(width - 20, height/2 - 70, 10, 140)
opponent = pg.Rect(10, height/2 - 70, 10, 140)

ball_speed_x = 7
ball_speed_y = 7

# main loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

  

    ball_animation()

    # adding color
    screen.fill(pg.Color('Silver'))
    pg.draw.ellipse(screen, pg.Color('Black'), ball)
    pg.draw.rect(screen, pg.Color('Grey9'), player)
    pg.draw.rect(screen, pg.Color('Grey9'), opponent)
    pg.draw.aaline(screen, pg.Color('Grey9'), (width/2, 0), (width/2, height))

    pg.display.flip()
    clock.tick(60)