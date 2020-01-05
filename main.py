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
PLAYER_SIZE = 40
BG_SPEED = 0.3
dx = 0

pygame.init()
pygame.display.set_caption('первая игра')
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

player = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
player.set_colorkey((0, 0, 0))
pygame.draw.circle(player, (0, 0, 250), (PLAYER_SIZE // 2, PLAYER_SIZE // 2), PLAYER_SIZE // 2)
pygame.draw.circle(player, (255, 215, 0), (12, 15), 4)
pygame.draw.circle(player, (255, 215, 0), (28, 15), 4)
pygame.draw.arc(player, (255, 215, 0), (8, 12, 24, 20), 3.6, 6.0, 3)
player_rect = player.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_rect.x += 3
    if keys[pygame.K_LEFT]:
        player_rect.x -= 3
    if keys[pygame.K_UP]:
        player_rect.y -= 3
    if keys[pygame.K_DOWN]:
        player_rect.y += 3

    screen.fill(BG_COLOR)

    dx -= BG_SPEED
    x = dx
    y = 0
    for row in level:
        for col in row:
            if col == '-':
                # screen.blit(brick, (x, y))
                brick = pygame.draw.rect(screen, BRICK_COLOR, [x, y, BRICK_WIDTH, BRICK_HEIGHT])
                pygame.draw.rect(screen, (255, 128, 0), [x, y, BRICK_WIDTH, BRICK_HEIGHT], 2)
                if brick.colliderect(player_rect):
                    print('!!!!!!!!!!', end=' ')
            x += BRICK_WIDTH
        y += BRICK_HEIGHT
        x = dx

    screen.blit(player, player_rect)
    pygame.display.set_caption(f' FPS: {round(clock.get_fps(), 2)}')
    pygame.display.update()
    clock.tick(FPS)
