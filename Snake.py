import pygame       
import random       # necessary libraries for the game to function

width = 600
height = 600
block_size = 20     # dimensions of game window, snake and food

pygame.font.init()
font_score = pygame.font.SysFont("Ariel", 20)
score = 0

white = (255, 255, 255)     # snake colour
green = (0, 255, 0)     # food colour

pygame.init()

window = pygame.display.set_mode((width, height))       # sets up display

clock = pygame.time.Clock()     # for frame rate

snake_position = [[width//2, height//2]]
snake_speed = [0, block_size]

teleport_walls = False  # if the snake runs into a wall, its game over. If this 
                        # was set to True, the snake would end up at the other side
                        # of the screen.

def generate_food():
    while True:
        x = random.randint(0, (width - block_size) // block_size) * block_size
        y = random.randint(0, (height - block_size) // block_size) * block_size
        food_position = [x, y]
        if food_position not in snake_position:
            return food_position

food_position = generate_food()

