import sys
import pygame
from game_window_class import *


WIDTH, HEIGHT = 800, 800
BACKGROUND = (199,199,199) #grey
FPS = 60

def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)


def update():
    game_window.update()
    
def draw():
    window.fill(BACKGROUND)
    game_window.draw()

def mouse_on_grid(pos):
    if pos[0] > 100 and pos[0] < WIDTH - 100:
        if pos[1] > 180 and pos[1] < HEIGHT - 20:
            # print('True')
            return True
    return 

def click_cell(pos): 
    grid_pos = [pos[0] - 100, pos[1-180]
    grid_pos[0] = grid_pos[0]//20
    grid_pos[1] = grid_pos[1]//20
    # pass in two list y x
    game_window.grid[grid_pos[[1]]][grid_pos[0]].alive = True

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game_window = Game_window(window, 50, 45)

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