import pygame,sys
from grid import Grid
from blocks import *

pygame.init()
dark_red = (127, 44, 44)

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game_grid = Grid()

block = ZBlock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Drawing
    screen.fill(dark_red)
    game_grid.draw(screen)
    block.draw(screen)

    pygame.display.update()
    clock.tick(60)