import pygame

level = [
    '--------------------------',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '--------------------------'
]

WIN_WIDTH, WIN_HEIGHT = 780, 630
BG_COLOR = (192, 192, 192)
# BRICK_WIDTH = BRICK_HEIGHT = 30
BRICK_WIDTH, BRICK_HEIGHT = 30, 30
BRICK_COLOR = (0, 128, 0)

pygame.init()
pygame.display.set_caption('первая игра')
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

brick = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
brick.fill(BRICK_COLOR)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False
       
    screen.fill(BG_COLOR)   

    x = 0
    y = 0
    for row in level:
        for col in row:
            if col == '-':
                screen.blit(brick, (x, y))
            x += BRICK_WIDTH
        y += BRICK_HEIGHT
        x = 0

    pygame.display.update()
