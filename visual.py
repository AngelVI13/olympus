import pygame
from itertools import chain, cycle

from mountain import Mountain

FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

TRIGGER_POINT_EVENT = pygame.USEREVENT + 1
TRIGGER_POINT_TIMER_MS = 500
pygame.time.set_timer(TRIGGER_POINT_EVENT, TRIGGER_POINT_TIMER_MS)

# circles = cycle(
circles = chain(
    (SCREEN_HEIGHT // i for i in range(2, 10)),
    (SCREEN_HEIGHT // i for i in reversed(range(2, 5))),
)

mountain = Mountain(list(circles), SCREEN_WIDTH, SCREEN_HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
        if event.type == TRIGGER_POINT_EVENT:
            mountain.trigger_point()

    screen.fill(pygame.Color("white"))

    mountain.draw(screen)
    # pygame.draw.rect(screen, pygame.Color("green"), (SCREEN_WIDTH//2, 100, SCREEN_WIDTH, 2))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
