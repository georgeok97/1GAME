import pygame
import sounddevice as sd
import numpy

level = [
    # '-' * int(WIN_WIDTH / BRICK_WIDTH),
    '----------------------------------------------------------------------------------------------------------------------------------',
    '-                           -                          --                        ---                                  -          -',
    '-                                                      --                                                       -                -',
    '-                                                                                                                                -',
    '-            --                                                   -                                                              -',
    '-                                                                                                                                -',
    '--                                                                -                                                              -',
    '-                                                                                   ---                                          -',
    '-                                       --                                          ---                                     ---  -',
    '-                                                                                                                                -',
    '-                                                                                                                                -',
    '-                                                                                 -                                              -',
    '-                                                     -                                                                          -',
    '-   --------                                          -                                                                          -',
    '-                                                                                                                  -             -',
    '-                                                                  --                                              -             -',
    '-                   --                                                                                                           -',
    '-                                                                             -                                  --              -',
    '-                                   -          -                             -                                  ---              -',
    '-                                   -                                       -                           -                        -',
    '----------------------------------------------------------------------------------------------------------------------------------']

WIN_WIDTH, WIN_HEIGHT = 780, 630
BG_COLOR = (192, 192, 192)
BRICK_WIDTH = BRICK_HEIGHT = 30
BRICK_COLOR = (0, 128, 0)
BRICK_COLOR_2 = (255, 128, 0)
FPS = 60
clock = pygame.time.Clock()
PLAYER_SIZE = 40
BG_SPEED = 3
dx = 0
PLAYER_SPEED = 3
penalty = 0.0
BTN_W, BTN_H = 220, 60
GOLD = (255, 215, 0)
BLUE = (0, 0, 255, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.display.set_caption('первая игра')
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

player = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
# player.set_colorkey((0, 0, 0))


def face(color):
    pygame.draw.circle(player, color, (PLAYER_SIZE // 2, PLAYER_SIZE // 2), PLAYER_SIZE // 2)
    pygame.draw.circle(player, GOLD, (12, 15), 4)
    pygame.draw.circle(player, GOLD, (28, 15), 4)
    pygame.draw.arc(player, GOLD, (8, 12, 24, 20), 3.6, 6.0, 3)


player_rect = player.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))

text = pygame.font.SysFont('Arial', 22, True, False)
text_xу = ((WIN_WIDTH - text.size(f'Штрафных очков: 0.0')[0]) // 2, 30)

btn = pygame.Surface((BTN_W, BTN_H))
btn.fill(BLUE)
text1 = 'ИГРАТЬ СНОВА ?'
text1_xy = ((BTN_W - text.size(text1)[0]) // 2, (BTN_H - text.size(text1)[1]) // 2)

result = [WIN_HEIGHT / 2.0]
yyy = [player_rect.y] * 100


def audio_callback(indata, frames, time, status):
    volume = numpy.linalg.norm(indata) * 20
    yyy.append(volume)
    yyy.pop(0)
    result[0] = sum(yyy) / len(yyy)


color = BLUE
face(color)
run = True
stream = sd.InputStream(callback=audio_callback)
with stream:
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                run = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    # print(mouse_pos)
                    if (
                        (WIN_WIDTH + BTN_W) // 2 > mouse_pos[0] > (WIN_WIDTH - BTN_W) // 2
                        and WIN_HEIGHT // 2 + BTN_H > mouse_pos[1] > WIN_HEIGHT // 2
                    ):
                        print('[INFO] Кнопка нажата, новая игра')
                        penalty = 0
                        dx = 0
                        player_rect.center = WIN_WIDTH // 2, WIN_HEIGHT // 2
                        result = [WIN_HEIGHT // 2]
                        yyy = [player_rect.y] * 20
                        color = BLUE
                        face(color)

        player_rect.y = WIN_HEIGHT - result[0]
        '''
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            player_rect.x += PLAYER_SPEED
        if keys[pygame.K_LEFT]:
            player_rect.x -= PLAYER_SPEED
        if keys[pygame.K_UP]:
            player_rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            player_rect.y += PLAYER_SPEED
        '''
        screen.fill(BG_COLOR)
        if color == RED:
            color = BLUE
            face(color)

        if dx > -WIN_WIDTH * 4:
            dx -= BG_SPEED
        else:
            if player_rect.x < WIN_WIDTH - PLAYER_SIZE:
                player_rect.x += PLAYER_SPEED

        x = dx
        y = 0
        for row in level:
            for col in row:
                if col == '-':
                    brick = pygame.draw.rect(screen, BRICK_COLOR, [x, y, BRICK_WIDTH, BRICK_HEIGHT])
                    pygame.draw.rect(screen, BRICK_COLOR_2, [x, y, BRICK_WIDTH, BRICK_HEIGHT], 2)
                    if brick.colliderect(player_rect):
                        if player_rect.x < WIN_WIDTH - PLAYER_SIZE * 2:
                            if color == BLUE:
                                color = RED
                                face(color)
                            penalty += 0.1
                x += BRICK_WIDTH
            y += BRICK_HEIGHT
            x = dx

        if player_rect.x < WIN_WIDTH - PLAYER_SIZE:
            screen.blit(player, player_rect)
            screen.blit(
                text.render(f'Штрафных очков: {round(penalty, 1)}', True, RED, None), text_xу)
        else:
            screen.blit(btn, ((WIN_WIDTH - BTN_W) // 2, WIN_HEIGHT // 2))
            btn.blit(
                text.render(text1, True, WHITE, None), text1_xy)
            screen.blit(
                text.render(f'Штрафных очков: {round(penalty, 1)}', True, RED, None),
                ((WIN_WIDTH - text.size(f'Штрафных очков: {round(penalty, 1)}')[0]) // 2,
                 WIN_HEIGHT // 2 - BTN_H))

        pygame.display.set_caption(f' FPS: {round(clock.get_fps(), 2)}')
        pygame.display.update()
        clock.tick(FPS)
