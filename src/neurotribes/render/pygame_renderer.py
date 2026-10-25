import pygame
def run_game():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_mode(size=(1000,700))
    pygame.display.set_caption("NeuroTribes")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(60)
    pygame.quit()