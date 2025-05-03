import pygame
from pygame.locals import *
import random
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Grow with me")

white = (255, 255, 255)
green = (100, 200, 100)
gray = (170, 170, 170)

font = pygame.font.SysFont('Arial', 36)

class Button:
    def __init__(self, x, y, text):
        self.text = text
        self.image = font.render(text, True, white)
        self.rect = self.image.get_rect(center = (x,y))
        self.color = green

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect.inflate(20, 20), border_radius=12)
        screen.blit(self.image, self.rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
start_button = Button(screen_width// 2, screen_height//2 - 60, "Start Growing")
shelf_button = Button(screen_width// 2, screen_height//2 + 60, "Shelf")

running = True
while running:
    screen.fill(gray)

    start_button.draw(screen)
    shelf_button.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.is_clicked(event.pos):
                print("Start Growing clicked!")
                # TODO switch to window 3
            if shelf_button.is_clicked(event.pos):
                print("Shelf clicked!")
                # TODO swithc to window 2
    
    pygame.display.update()

pygame.quit()
sys.exit()