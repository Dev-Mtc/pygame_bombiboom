import pygame

pygame.init()


FONT_SIZE_HEAL = 25
FONT_SIZE_SHIELD = 25


class Interface:
    def __init__(self):
        self.heal_value = 0
        
    def draw_heal_bar(self,  value: int,surface: pygame.surface.Surface):
        if value > 50 :
            self.color =  (39, 100, 0)
            self.border_color = (39, 127, 0)
        elif value < 50 and value > 25 :
            self.color = (161,74,8)
            self.border_color = (141,82,5)
        elif value < 25: 
            self.color = (198,45,7)
            self.border_color = (220,60,20)
        
        
        #init font 
        self.font_heal = pygame.font.SysFont("assets/fonts/good_times_rg.otf", FONT_SIZE_HEAL)
        self.img_value_heal = self.font_heal.render(str(value) , True, self.color)
        
        # Draw font and interface
        surface.blit(self.img_value_heal, (240, 52))
        self.heal_bar_border = pygame.draw.rect(surface,self.border_color  , pygame.Rect(30, 50, 200, 20), 1 , border_radius=5)
        self.heal_bar = pygame.draw.rect(surface,self.color, pygame.Rect(30, 50, value*2, 20), border_radius=5)
        
    def draw_shield_bar(self, value: int,surface: pygame.surface.Surface):
        self.shield_color = (51, 153, 255)
        
        
        self.font_shield = pygame.font.SysFont("assets/fonts/good_times_rg.otf", FONT_SIZE_SHIELD)
        self.img_value_shield = self.font_shield.render(str(value) , True, self.shield_color)
        
        # Draw font and interface
        surface.blit(self.img_value_shield, (240, 92))
        self.shield_bar_border = pygame.draw.rect(surface,self.shield_color  , pygame.Rect(30, 90, 200, 20), 1, border_radius=5)
        self.shield_bar = pygame.draw.rect(surface,self.shield_color, pygame.Rect(30, 90, value*2, 20), border_radius=5)
