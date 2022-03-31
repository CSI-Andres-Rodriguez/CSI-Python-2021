# acces the script from another Python file
import pygame
# Allows to work with time in Python
import time
#initiates the game
pygame.init()
 
 # Different RBG. RGB describes a color as a tuple of three components.
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 102)
green = (0, 255, 0)
blue = (50, 153, 213)
brown = (92, 42, 42)
pink = (238, 32, 224)
purple = (135, 32, 238)

#The dis module includes functions for working with Python bytecode by “disassembling” it into a more human-readable form.
#width
dis_width = 600
#height
dis_height  = 500

#This control displays a list of items for the user to select. The items parameter must be a Python list. It can contain as many items as you wish.
# 
dis = pygame.display.set_mode((dis_width, dis_width))
#Shows or display the name of the game (Snake Game by Edureka)
pygame.display.set_caption('Snake Game by Edureka')
 
 #it will do a variable name "game over" that has a value of false
game_over = False
 
x1 = dis_width/2
y1 = dis_height/2
 
snake_block=15  
 
x1_change = 0
y1_change = 0
 
 #Clock of Snake Game by Edureka
clock = pygame.time.Clock()
#The speed of the snake is 20
snake_speed=20
 
font_style = pygame.font.SysFont(None, 50)
 
 #Define the message
def message(msg,color): 
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
 
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True
 
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
 
    pygame.display.update()
 
    clock.tick(snake_speed)
 
message("You lost",red)
pygame.display.update()
time.sleep(2)
 
pygame.quit()
quit()

