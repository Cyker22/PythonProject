import pygame
import random
import sys

pygame.init()
WIDTH,HEIGHT =600,400
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
CLOCK = pygame.time.Clock()

WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLACK=(0,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

BLOCK_SIZE = 20

def game():
    x, y = WIDTH//2,HEIGHT//2
    dx, dy = BLOCK_SIZE,0
    snake = [(x,y)]
    food =(random.randrange(0,WIDTH-BLOCK_SIZE),
           random.randrange(0,HEIGHT-BLOCK_SIZE))
score = 0
running = True
while running:
        CLOCK.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and dy == 0:
                        dx,dy = BLOCK_SIZE,0
                    elif event.key == pygame.K_LEFT and dy == 0:
                        dx,dy = -BLOCK_SIZE,0
                    elif event.key == pygame.K_RIGHT  and dx == 0:
                        dx, dy = BLOCK_SIZE,0
                    elif event.key == pygame.K_DOWN and dy == 0:
                        dx, dy = BLOCK_SIZE,0

                        x+=dx
                        y+=dy
                        #collision with walls
                        if x<0 or x>=WIDTH or y<0 or y>=HEIGHT:
                            running = False

                            snake=insert(0,(x,y))

                            #eat food
                            if (x,y) == food:
                                score += 1
                                food=(random.randrange(0,WIDTH-BLOCK_SIZE),
                                      random.randrange(0,HEIGHT-BLOCK_SIZE))
                            else:
                                snake

