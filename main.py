import pygame
import numpy as np

pygame.init()

#set up display
width, height = 900,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong game by rabio")
running = True

#defining and intializing variables of the brackets
rect_width = 5
rect_height = 200
rect1_x = 870
rect2_x = 30
rect1_y = 200
rect2_y = 200
rect_speed = 1
#initializing variables of the ball
circle_x = 400
circle_y = 300

#the speed of mouvment of the game (brackets) 
speed = 0.5

#just initialization
up_key_pressed = False
down_key_pressed = False
z_key_pressed = False
s_key_pressed = False

#main game loop
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #conditionnals to detect a pressing of a key by using KEYDOWN, if it's there a press we store True in var corresponding to the key
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up_key_pressed = True
            if event.key == pygame.K_DOWN:
                down_key_pressed = True
            if event.key == pygame.K_z:
                z_key_pressed = True
            if event.key == pygame.K_s:
                s_key_pressed = True
        #conditionnal to detect end of pressing of a key, this with the previous if are necessary to detect continious pressing of button 
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

    #it's here and not outside while to update the frame everytime with a new image and not superpose images ontop of each other
    screen.fill((0,0,0))
    #to draw the brackets
    pygame.draw.rect(screen,(255,255,255),(rect1_x,rect1_y,rect_width,rect_height),rect_width)
    pygame.draw.rect(screen,(255,255,255),(rect2_x,rect2_y,rect_width,rect_height),rect_width)
    #to draw the ball
    pygame.draw.circle(screen,(250,250,250),(circle_x,circle_y),10,10)

    #setting the circle to move permanently in x-axis direction by incrementing it's x position by "speed"
    circle_x += speed
    #conditionnals to limit the movement of the ball just inside the screen, and setting a colision if the ball reach each side
    if circle_x > 870:
        speed = -speed
    if circle_x < 30:
        speed = -speed
    
    #setting the actions done by each key pressed on the brackets to move, and limiting their movement just in the screen and not get outside
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
