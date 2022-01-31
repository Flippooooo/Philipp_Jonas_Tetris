
from curses import KEY_DOWN
import pygame


pygame.init()
pygame.display.set_mode((400, 500))
pygame.display.set_caption("Tetris")

done = False
fps = 25
clock = pygame.time.Clock()
counter = 0  

game = Tetris()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate() 
            if event.key == pygame.K_DOWN:
                game.down()
            if event.key == pygame.K_LEFT:
                game.left()
            if event.key == pygame.K_RIGHT:
                game.right()
        if event.key ==     

pygame.quit