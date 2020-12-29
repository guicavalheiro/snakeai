import pygame
from screen import Game
import time



def main():

    background_color = (255, 255, 255)
    window_height    = 1000
    window_width     = 1750

    canvas_height    = 750
    canvas_width     = 1250

    g = Game()
    g.create_screen(window_width, window_height)
    g.screen.fill(background_color)

    g.create_surface(canvas_width, canvas_height)
    g.create_cells()
    g.add_player()

    g.food_in_place()

    clock = pygame.time.Clock()

    run = True
    while run:

        clock.tick(60)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    g.move_player("l")
                
                elif event.key == pygame.K_RIGHT:
                    g.move_player("r")

                elif event.key == pygame.K_UP:
                    g.move_player("u")

                elif event.key == pygame.K_DOWN:
                    g.move_player("d")

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

