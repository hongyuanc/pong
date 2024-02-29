import pygame as pg
import sys
import random

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
        restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= height:
        player.bottom = height

def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= height:
        opponent.bottom = height

def restart():
    ball.center = (width/2, height/2)
    ball_speed_y = random.choice((1, -1))
    ball_speed_x = random.choice((1, -1))

# shape and its dimentions
ball = pg.Rect(width/2 - 15, height/2 - 15, 30, 30)
player = pg.Rect(10, height/2 - 70, 10, 140)
opponent = pg.Rect(width - 20, height/2 - 70, 10, 140)


ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 7

# main loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                player_speed += 7
            if event.key == pg.K_UP:
                player_speed -= 7
        if event.type == pg.KEYUP:
            if event.key == pg.K_DOWN:
                player_speed -= 7
            if event.key == pg.K_UP:
                player_speed += 7
    
    ball_animation()
    player_animation()
    opponent_animation()

    # adding color
    screen.fill(pg.Color('Silver'))
    pg.draw.ellipse(screen, pg.Color('Black'), ball)
    pg.draw.rect(screen, pg.Color('Grey9'), player)
    pg.draw.rect(screen, pg.Color('Grey9'), opponent)
    pg.draw.aaline(screen, pg.Color('Grey9'), (width/2, 0), (width/2, height))

    pg.display.flip()
    clock.tick(60)