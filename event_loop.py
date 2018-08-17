from pygame.locals import KEYDOWN
import pygame


def event_loop(handle_key, delay=10):
    while True:
        pygame.event.pump()
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            handle_key(event.key)
        pygame.time.delay(delay)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_mode((640, 400))
    event_loop(print)
