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
FPS = 60
clock = pygame.time.Clock()
x1, y1 = WIN_WIDTH // 2, WIN_HEIGHT // 2
PLAYER_SIZE = 50

pygame.init()
pygame.display.set_caption('первая игра')
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

player = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
player.set_colorkey((0, 0, 0))
# brick.fill(BRICK_COLOR)

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
                # screen.blit(brick, (x, y))
                brick = pygame.draw.rect(screen, BRICK_COLOR, [x, y, BRICK_WIDTH, BRICK_HEIGHT])
                pygame.draw.rect(screen, (255, 128, 0), [x, y, BRICK_WIDTH, BRICK_HEIGHT], 2)
            x += BRICK_WIDTH
        y += BRICK_HEIGHT
        x = 0

    screen.blit(player, (x1, y1))
    pygame.display.set_caption(f' FPS: {round(clock.get_fps(), 2)}')
    pygame.display.update()
    clock.tick(FPS)
