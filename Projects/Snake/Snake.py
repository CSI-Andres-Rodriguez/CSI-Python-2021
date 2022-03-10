import pygame #imports pygame
pygame.init() #initiates the game
dis=pygame.display.set_mode((400,300)) #the size of the display of the game
pygame.display.update() # play the game
pygame.quit() # finished the game
quit() # game finished

#white = (255, 255, 255)
#yellow = (255, 255, 102)
#black = (0, 0, 0)
#red = (213, 50, 80)
#green = (0, 255, 0)
#blue = (50, 153, 213)
#brown = (92, 42, 42)
#pink = (238, 32, 224)
#purple = (135, 32, 238)
  
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 