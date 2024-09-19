import pygame
import random
pygame.init()

SCREEN_WIGTH = 800
SCREEN_HEIGHT = 600
screnn = pygame.display.set_mode((SCREEN_WIGTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/тир.PNG")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIGTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



running = True
while running:
    pass
pygame.quit()


