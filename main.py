import pygame
import random

pygame.init()

SCREEN_WIGTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIGTH, SCREEN_HEIGHT))  # Исправлено

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
    screen.fill(color)  # Используем правильную переменную 'screen'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Исправлено условие для клика по мишени
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIGTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_img, (target_x, target_y))

    pygame.display.update()

pygame.quit()


