import pygame
from pygame.locals import *
import random
import sys

pygame.init()

screen_width = 800
screen_height = 533
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Grow with me")

bg = pygame.image.load('img/back.png')
background_img = pygame.transform.scale(bg, (screen_width, screen_height))


white = (255, 255, 255)
green = (100, 200, 100)
gray = (170, 170, 170)

font = pygame.font.SysFont('Bauhuas 93', 36)

class GlassButton:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.base_color = (255, 255, 255, 100) 
        self.hover_color = (255, 255, 255, 140)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('Arial', 30)
        self.hovered = False

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        self.hovered = self.rect.collidepoint(mouse_pos)

        button_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        color = self.hover_color if self.hovered else self.base_color
        pygame.draw.rect(button_surface, color, button_surface.get_rect(), border_radius=15)
        surface.blit(button_surface, self.rect.topleft)

        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
start_button = GlassButton(screen_width// 2-100, screen_height//2 -30,200, 60, "Start Growing")
shelf_button = GlassButton(screen_width// 2 + 200, screen_height//2 + 170, 150, 50,"Shelf")

running = True
while running:
    screen.blit(bg, (0,0))

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