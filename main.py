import pygame
import numpy as np

pygame.init()

#set up display
width, height = 900,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong game by rabio")
running = True

#defining and intializing some variables
rect_width = 5
rect_height = 200
rect1_x = 870
rect2_x = 30
rect1_y = 200
rect2_y = 200

circle_x = 400
circle_y = 300

speed = 0.5
rect_speed = 1

up_key_pressed = False
down_key_pressed = False
z_key_pressed = False
s_key_pressed = False

#main game loop
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up_key_pressed = True
            if event.key == pygame.K_DOWN:
                down_key_pressed = True
            if event.key == pygame.K_z:
                z_key_pressed = True
            if event.key == pygame.K_s:
                s_key_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_key_pressed = False
            if event.key == pygame.K_DOWN:
                down_key_pressed = False
            if event.key == pygame.K_z:
                z_key_pressed = False
            if event.key == pygame.K_s:
                s_key_pressed = False
            
    #the actual game
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),(rect1_x,rect1_y,rect_width,rect_height),rect_width)
    pygame.draw.rect(screen,(255,255,255),(rect2_x,rect2_y,rect_width,rect_height),rect_width)

    pygame.draw.circle(screen,(250,250,250),(circle_x,circle_y),10,10)

    circle_x += speed
    if circle_x > 870:
        speed = -speed
    if circle_x < 30:
        speed = -speed
        
    if up_key_pressed:
        if rect1_y > 0:
            rect1_y -= rect_speed
    if down_key_pressed:
        if rect1_y < 600 - rect_height:
            rect1_y += rect_speed
    if z_key_pressed:
        if rect2_y > 0:
            rect2_y -= rect_speed
    if s_key_pressed:
        if rect2_y < 600 - rect_height:
            rect2_y += rect_speed
    

    pygame.display.update()
