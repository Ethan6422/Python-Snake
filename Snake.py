from turtle import position

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

def draw_objects():
    window.fill((0, 0, 0,))
    for position in snake_position:
        pygame.draw.rect(window, white, pygame.Rect(position[0], position[1], block_size, block_size))
    pygame.draw.rect(window, green, pygame.Rect(food_position[0], food_position[1], block_size, block_size))
    score_text = font_score.render(f"Score: {score}", True, white)
    window.blit(score_text, (10, 10)) # places score on top-left

def move_snake():
    global food_position, score
    new_head = [snake_position[0][0] + snake_speed[0], snake_position[0][1] + snake_speed[1]]

    if teleport_walls == True:      # if the snake runs into a wall, it will
        if new_head[0] >= width:    # wrap around to the other 
            new_head[0] = 0         # side of the screen. This code only
        elif new_head[0] < 0:       # runs if teleport_walls on line 24 is
            new_head[0] = width - block_size    # set to True.
        if new_head[1] >= height:
            new_head[1] = 0
        elif new_head[1] < 0:
            new_head[1] = height - block_size

    if new_head == food_position:
        food_position = generate_food()
        score += 1
    else:
        snake_position.pop()  # removes the last segment of the snake if 
                              # it hasn't eaten food

    snake_position.insert(0, new_head)  # adds the new head to the snake's 
                                        # position

def game_over():