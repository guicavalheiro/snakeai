import pygame
from pygame.locals import * 
import time
import random

class Game:

    def __init__(self):
        
        # Initialize the game
        pygame.init()
        pygame.font.init()

        # Set title of screen
        pygame.display.set_caption("Snake")

        # Initializing font test
        self.font = pygame.font.SysFont('Arial', 15)
        self.id = 1

        self.mock_food = True

    def create_screen(self, width, height):

        self.window_width  = width
        self.window_height = height

        self.screen = pygame.display.set_mode([self.window_width, self.window_height])
    
    def create_surface(self, width, height):

        self.canvas_width  = width
        self.canvas_height = height

        self.canvas = pygame.Surface([self.canvas_width, self.canvas_height])
        self.screen.blit(self.canvas, (self.window_width / 2 - self.canvas_width / 2, self.window_height / 2 - self.canvas_height / 2))

        self.edge_width  = width + 10
        self.edge_height = height + 10

        self.edge = pygame.Surface([self.edge_width, self.edge_height])
        self.screen.blit(self.edge, (self.window_width / 2 - self.edge_width / 2, self.window_height / 2 - self.edge_height / 2))

    def create_cells(self):

        # 25 x 15

        cell_width  = 50
        cell_height = 50

        x = self.window_width / 2 - self.canvas_width / 2
        y = self.window_height / 2 - self.canvas_height / 2
    
        cell_coords  = [x, y, cell_width, cell_height]
        cell_color   = [255, 255, 255]  
 
        bool_ = True

        self.grid = {}

        x_grid = int(self.canvas_width  / cell_width)
        y_grid = int(self.canvas_height / cell_height)

        for column in range(y_grid):
            for row in range(x_grid):
            
                #print(f"({x}, {y})")

                # if bool_:
                #     cell_color = [94, 191, 226]
                #     bool_ = False
                # else:
                #     cell_color = [50, 50, 30]
                #     bool_ = True

                cell_coords[0] = x
                cell_coords[1] = y

                #print(f"\nCell Coords: {cell_coords}")
                cell_object = Cell(self.id, [x, y, cell_width, cell_height], cell_color)
            
                #print(f"Cell object: {cell_object.coords}")

                self.grid[f'{x}, {y}'] = cell_object

                pygame.draw.rect(self.screen, cell_color, cell_coords)
                # self.screen.blit(self.font.render(f'{cell_object.id}', True, [0, 0, 0]), [cell_object.coords[0], cell_object.coords[1]])
                
                self.id += 1
                x += 50

                # time.sleep(0.05)
                # pygame.display.update()
            
            y += 50
            x = self.window_width / 2 - self.canvas_width / 2
                
        pygame.display.update()

        # print("\n")
        # for key in self.grid:
        #     print(f"Key: {key}\tContent: {self.grid[key].coords}")
        # print("\n")
            
    def add_player(self):
        
        player_width  = 50
        player_height = 50

        initial_x = self.window_width / 2 - self.canvas_width / 2
        initial_y = self.window_height / 2 + self.canvas_height / 2 - player_width
        
        self.player = Player(initial_x, initial_y, player_width, player_height, [255, 0, 0])
        
        # Start score
        self.display_score = pygame.font.SysFont('Arial', 40)
        self.screen.blit(self.display_score.render(f'Pontuação: {self.player.score}', True, [0, 0, 0]), [0, 0])
        
        # Draw player
        print(f"Starting in      : {self.player.x}, {self.player.y}, ID: {self.grid[f'{self.player.x}, {self.player.y}'].id}")
        self.player.body.append([self.player.x, self.player.y])
        pygame.draw.rect(self.screen, self.player.color, [self.player.x, self.player.y, self.player.width, self.player.height])
        pygame.display.update()

    def update_score(self, score):

        self.player.score += score
        # self.player.body += 1

        pygame.draw.rect(self.screen, [255, 255, 255], [0, 0, 1000, 50])
        pygame.display.update()

        self.screen.blit(self.display_score.render(f'Pontuação: {self.player.score}', True, [0, 0, 0]), [0, 0])
        pygame.display.update()

    # def grow_snake(self, coords):
        
    #     self.player.body += 1

    def found_food(self, next_cell):
        
        print("Comeu!")
        self.player.color = [0, 0, 0]
        next_cell.food = False
        self.food_in_place()
        self.update_score(1000)

    def grow_snake(self, key):
        
        if key == 'u':
            
            if len(self.player.body) < 2:
                body_coords = self.player.body[0]
                body_coords[1] -= 50
                self.player.body.append([body_coords[0], body_coords[1]])
                print(f"Growing in {body_coords[0], body_coords[1]}")
                pygame.draw.rect(self.screen, self.player.color, [body_coords[0], body_coords[1], self.player.width, self.player.height]) 

        # elif key == 'r':
     
        #    if len(self.player.body) < 2:
        #         self.player.body['tail'] = 
        
        # elif key == 'd':

        #    if len(self.player.body) < 2:
        #         self.player.body['tail'] = 
    
        # elif key == 'l':

        #    if len(self.player.body) < 2:
        #         self.player.body['tail'] = 

        

    def move_player(self, key):
        
        pos_x = self.player.x
        pos_y = self.player.y
        
        x0 = self.window_width  / 2 - self.canvas_width  / 2
        y0 = self.window_height / 2 - self.canvas_height / 2
        
        xF = self.window_width  / 2 + self.canvas_width  / 2 - self.player.width
        yF = self.window_height / 2 + self.canvas_height / 2 - self.player.height

        if key == 'u':
            
            if pos_y == y0:
                print("Trying to go out of bounds")
            
            else:
                
                # Previous cell details
                # prev_cell = self.grid[f'{pos_x}, {pos_y}']
                
                # # Redrawing occupied cell
                # pygame.draw.rect(self.screen, prev_cell.color, [pos_x, pos_y, self.player.width, self.player.height])

                # Next cell details
                
                
                
                

                # self.grow_snake()
    
                # Moving player, first drawing head
                # self.player.y -= 50
                # pygame.draw.rect(self.screen, [120, 120, 120], [self.player.x, self.player.y, self.player.width, self.player.height])
                
                # body_drawing = self.player.y
                
                new_y = self.player.y - 50

                for body_part in range(len(self.player.body)):
                    print(f"\nDesenhando body {body_part}: {self.player.body[body_part]}")
                    
                    if body_part == 0:
                        # PAREI AQUI, SALVAR POSIÇÃO ANTIGA PARA PASSAR PARA O PROXIMO
                        
                        previous_x = self.player.body[body_part][0]
                        previous_y = self.player.body[body_part][1]

                        body_coords = self.player.body[body_part]
                        body_coords[1] = body_coords[1] - 50

                    else:

                    print(f"Moving player to: {body_coords[0]}, {body_coords[1]}")

                    # Drawing body
                    # body_drawing += 50
                    pygame.draw.rect(self.screen, self.player.color, [body_coords[0], body_coords[1], self.player.width, self.player.height])
                    
                    # Redrawing occupied cell
                    prev_cell = self.grid[f'{previous_x}, {previous_y}']
                    pygame.draw.rect(self.screen, prev_cell.color, [prev_cell.coords[0], prev_cell.coords[1], self.player.width, self.player.height])
                    
                    self.player.body[body_part] = body_coords
                    print(f"New coords: {self.player.body[body_part]}")
                    next_cell = next_cell = self.grid[f'{body_coords[0]}, {body_coords[1]}']
                    if next_cell.food and body_part == 0:
                        self.found_food(next_cell)
                        self.grow_snake(key)

        elif key == 'r':
            
            if pos_x == xF:
                print("Trying to go out of bounds")
            
            else:
                
                # Previous cell details
                prev_cell = self.grid[f'{pos_x}, {pos_y}']
                
                # Redrawing occupied cell
                pygame.draw.rect(self.screen, prev_cell.color, [pos_x, pos_y, self.player.width, self.player.height])

                # Next cell details
                next_cell = self.grid[f'{pos_x + 50}, {pos_y}']
                
                print(f"Next Cell : {next_cell.coords}")
                if next_cell.food:
                    self.found_food(next_cell)
                    
                # Moving player, first drawing head
                self.player.x += 50
                pygame.draw.rect(self.screen, self.player.color, [self.player.x, self.player.y, self.player.width, self.player.height])

                body_drawing = self.player.x
                for body in range(self.player.body - 1):
                    print(f"Desenhando body: {body}")
                    
                    # Drawing body
                    body_drawing -= 50
                    pygame.draw.rect(self.screen, self.player.color, [body_drawing, self.player.y, self.player.width, self.player.height])

                    # Redrawing occupied cell
                    prev_cell = self.grid[f'{pos_x - (50 * (body + 1))}, {pos_y}']
                    pygame.draw.rect(self.screen, prev_cell.color, [prev_cell.coords[0], prev_cell.coords[1], self.player.width, self.player.height])
                
        elif key == 'd':
            
            if pos_y == yF:
                print("Trying to go out of bounds")
            
            else:
               
                # Previous cell details
                prev_cell = self.grid[f'{pos_x}, {pos_y}']

                # Redrawing occupied cell
                pygame.draw.rect(self.screen, prev_cell.color, [pos_x, pos_y, self.player.width, self.player.height])

                # Next cell details
                next_cell = self.grid[f'{pos_x}, {pos_y + 50}']
                
                print(f"Next Cell : {next_cell.coords}")
                if next_cell.food:
                    self.found_food(next_cell)

                # Moving player, first drawing head
                self.player.y += 50
                pygame.draw.rect(self.screen, [120, 120, 120], [self.player.x, self.player.y, self.player.width, self.player.height])

                body_drawing = self.player.y
                for body in range(self.player.body - 1):
                    print(f"Desenhando body: {body}")
                    
                    # Drawing body
                    body_drawing -= 50
                    pygame.draw.rect(self.screen, self.player.color, [self.player.x, body_drawing, self.player.width, self.player.height])
                    
                    # Redrawing occupied cell
                    prev_cell = self.grid[f'{pos_x}, {pos_y - (50 * (body + 1))}']
                    pygame.draw.rect(self.screen, prev_cell.color, [prev_cell.coords[0], prev_cell.coords[1], self.player.width, self.player.height])

        elif key == 'l':
            
            if pos_x == x0:
                print("Trying to go out of bounds")
            
            else:
                
                # Previous cell details
                prev_cell = self.grid[f'{pos_x}, {pos_y}']

                # Redrawing occupied cell
                pygame.draw.rect(self.screen, prev_cell.color, [pos_x, pos_y, self.player.width, self.player.height])

                # Next cell details
                next_cell = self.grid[f'{pos_x - 50}, {pos_y}']
                
                print(f"Next Cell : {next_cell.coords}")
                if next_cell.food:
                    self.found_food(next_cell)
    
                # Moving player, first drawing head
                self.player.x -= 50
                pygame.draw.rect(self.screen, self.player.color, [self.player.x, self.player.y, self.player.width, self.player.height])

                body_drawing = self.player.x
                for body in range(self.player.body - 1):
                    print(f"Desenhando body: {body}")
                    
                    # Drawing body
                    body_drawing -= 50
                    pygame.draw.rect(self.screen, self.player.color, [body_drawing, self.player.y, self.player.width, self.player.height])

                    # Redrawing occupied cell
                    prev_cell = self.grid[f'{pos_x + (50 * (body + 1))}, {pos_y}']
                    pygame.draw.rect(self.screen, prev_cell.color, [prev_cell.coords[0], prev_cell.coords[1], self.player.width, self.player.height])

        pygame.display.update()
    
    def food_in_place(self):
        
        # print("\n")
        # for key in self.grid:
        #     print(f"Key: {key}\tContent: {self.grid[key].coords}")
        # print("\n")

        if self.mock_food:
            choosen_cell = '250.0, 725.0'
            self.mock_food = False

        else:

            coords = list(self.grid.keys())
            
            choosen_cell = random.randint(0, len(coords) - 1)
            # print(f"Choosen Cell randint: {choosen_cell}")
        
            choosen_cell = coords[choosen_cell]
        # print(f"Choosen Cell coords : {choosen_cell}")
        choosen_cell = self.grid[choosen_cell]
        # print(f"Food Cell grid   : {choosen_cell.coords}\nID                  : {choosen_cell.id}")
        choosen_cell.food = True

        food_width  = 10
        food_height = 10

        #print([choosen_cell.coords[0], choosen_cell.coords[1], food_width, food_height])

        food_x      = choosen_cell.coords[0]
        food_y      = choosen_cell.coords[1]

        # food_x      = (choosen_cell.coords[0] - choosen_cell.coords[2] / 2) - food_width  / 2
        # food_y      = (choosen_cell.coords[1] - choosen_cell.coords[3] / 2) - food_height / 2

        # print(f"Coords finais: {[food_x, food_y, food_width, food_height]}")

        pygame.draw.rect(self.screen, [51, 204, 51], [food_x, food_y, food_width, food_height])
        pygame.display.update()

class Player:

    def __init__(self, x, y, width, height, color):

        self.x = x
        self.y = y

        self.width  = width
        self.height = height

        self.color = color
    
        self.body = []

        self.score = 0

class Cell:

    def __init__(self, id_, coords, color):
        
        self.id = id_
        self.coords = coords
        self.color = color
        self.food = False