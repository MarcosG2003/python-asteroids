import pygame 
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids with pygame version: %s"% pygame.version.ver)
    print("Screen width: %s"% SCREEN_WIDTH)
    print("Screen height: %s"% SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    fps = 60

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        player.draw(screen)

        pygame.display.flip()
        tim = clock.tick(fps)
        dt = tim / 1000
        
    

if __name__ == "__main__":
    main()
