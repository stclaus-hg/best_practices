import pygame


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_mode((640, 400))
    while True:
        pygame.event.pump()
        event = pygame.event.poll()
        print(event)
