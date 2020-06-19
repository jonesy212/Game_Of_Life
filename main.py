import pygame
import sys
from game_window_class import *


WIDTH, HEIGHT = 800, 800
BACKGROUND = (28, 88, 32)
FPS = 60

WIDTH, HEIGHT = 800, 800
BACKGROUND = (199,199,199) #grey
FPS = 60

pygame.init()

def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

def update():
    # game_window.update()
    pass

def draw():
    # game_window.draw()
    display.fill(BACKGROUND)
    
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# game_window = game_window(display, x, y)

running = True
while running:
    get_events()
    update()
    draw()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()



#grid of cells
#alive black
#dead white

#rules

# Live black box
# Die white box

# Rule for death
# If a cell has two neighbors, it will live
# If a cell has one neighbor, it will die

# Example
# If a cell is in between two cell s ( 1 2 1)
# The middle 2 lives and the two ones will die


# Rule for birth
# If a cell has exactly 3 live neighbors, it lives ( touchin on three sides)