# access the script from another Python file
import pygame
#initiates the game
pygame.init()
#the size of the display of the game
dis=pygame.display.set_mode((400,300))
#it refresh the game and the screen
pygame.display.update()
# 
pygame.quit()

# access the script from another Python file
import pygame
#initiates the game
pygame.init() 
#the size of the display of the game
dis=pygame.display.set_mode((400,300)) 
#name of the game
pygame.display.set_caption('Snake game by Edureka')
# it will do a variable name "game over" that has a value of false
game_over=False
# if the value was not false then do a loop
while not game_over: 
    # event is a temporary variable that represent every variable on the pygame list (forloop)
    for event in pygame.event.get():
        # if the game find an envent that finished the game and change te value of the varieable to true
        if event.type==pygame.QUIT:
            # the value of the variable is true
            game_over=True
        # if the value is not false then do a loop and prints out all the actions that take place on the screen
        print(event)
# game finished

#white = (255, 255, 255) 
#yellow = (255, 255, 102)
#black = (0, 0, 0)
#red = (213, 50, 80)
#green = (0, 255, 0)
#blue = (50, 153, 213)
#brown = (92, 42, 42)
#pink = (238, 32, 224)
#purple = (135, 32, 238)
  

import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('Snake game by Edureka')
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
 
pygame.quit()
quit()
