import pygame, sys

# setup
pygame.init()
clock = pygame.time.Clock()

# setting up the window
width = 1280
height = 920
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)