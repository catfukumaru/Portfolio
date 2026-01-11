import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((900, 640))

rect_w, rect_h = 100, 100

# title = pygame.image.load('Galaxy.png').convert()
# title = pygame.transform.scale_by(title, 3)

pygame.display.set_caption("Sample Start UI")

play_button = pygame.image.load('arrow_right.png').convert_alpha()

play_button = pygame.transform.scale_by(play_button, 6).convert_alpha()


# Load background image
background_image = pygame.image.load('Background.png')
#print(background_image.get_size()) 

#objects = [title, play_button ]
#objects_coor = []

game_loop = True
clock = pygame.time.Clock()

# find the center coordinates
screen_rect = screen.get_rect()
center_x, center_y = screen_rect.center

center_y_arrow_right = center_y + 100
# to center things the x is the same but the y is diffrent
pos_y_play_button = (center_y_arrow_right - play_button.get_height() // 2) 
y_current_pos = pos_y_play_button
# making the arrow bounce
going_up = True



## have text as the title
font = pygame.font.Font("RetroByte.woff", size=96)
title= font.render("Sample Start UI", True, (255, 255, 255)).convert_alpha()

#largeText = pygame.font.Font('freesansbold.ttf', 100) # the font

while game_loop:
    screen.blit(background_image, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False


    #screen.blit(background_image, (0,0))

    if going_up:
        y_current_pos -= 1
        if y_current_pos <= center_y_arrow_right - (20):
            going_up = False
    else:
        y_current_pos += 1
        if y_current_pos >= center_y_arrow_right + 20:
            going_up = True

    pos_x_title = (center_x - title.get_width()) // 2 +250 # +250 find  a fix for this
    pos_x_play_button = center_x - play_button.get_width() // 2

    pos_y_title = (center_y - title.get_height() // 2) 
    #pos_y_play_button = (center_y - play_button.get_height() // 2) + 100

    screen.blit(title, (pos_x_title, pos_y_title- 150))
    screen.blit(play_button, (pos_x_play_button, y_current_pos - rect_h // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()