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
        surface.blit(self.img_value_heal, ((surface.get_width()/2 + 110), (surface.get_height()- 40)))
        self.heal_bar_border = pygame.draw.rect(surface,self.border_color  , pygame.Rect((surface.get_width()/2 - 100), (surface.get_height()- 40), 200, 20), 1 , border_radius=5)
        self.heal_bar = pygame.draw.rect(surface,self.color, pygame.Rect((surface.get_width()/2 - 100), (surface.get_height()- 40), value*2, 20), border_radius=5)
        
    def draw_shield_bar(self, value: int, surface: pygame.surface.Surface):
        self.shield_color = (51, 153, 255)
        
        
        self.font_shield = pygame.font.SysFont("assets/fonts/good_times_rg.otf", FONT_SIZE_SHIELD)
        self.img_value_shield = self.font_shield.render(str(value) , True, self.shield_color)
        
        # Draw font and interface
        surface.blit(self.img_value_shield, ((surface.get_width()/2 +110), (surface.get_height()- 70)))
        self.shield_bar_border = pygame.draw.rect(surface,self.shield_color  , pygame.Rect((surface.get_width()/2 - 100), (surface.get_height()- 70), 200, 20), 1, border_radius=5)
        self.shield_bar = pygame.draw.rect(surface,self.shield_color, pygame.Rect((surface.get_width()/2 - 100), (surface.get_height()- 70), value*2, 20), border_radius=5)
        
        
        

class Button: 
    def __init__(self, x, y, width, height, content,font_size, bg_color, hover_color):
        self.x_pos = x
        self.y_pos = y
        self.width_button = width
        self.height_button = height
        
        self.color = bg_color
        self.hover_color = hover_color
        self.content = content
        
        
        
        self.rect_btn = pygame.Surface((self.width_button, self.height_button))
        self.rect_btn.fill(self.color)
        self.rect = self.rect_btn.get_rect()
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos
       
        #init font 
        self.font = pygame.font.SysFont("assets/fonts/good_times_rg.otf", font_size)
        self.text_btn = self.font.render(str(content) , True, (0,0,0))
        
        self.rect_btn.blit(self.text_btn, (self.text_btn.get_rect(center=(self.width_button/2, self.height_button/2))))
        
    def is_pressed(self, mouse_pos, mouse_pressed : bool):
        if self.rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            return True
        return False
    
    def is_hovering(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.rect_btn.fill(self.hover_color)
            self.text_btn = self.font.render(str(self.content) , True, (0,0,0))
            self.rect_btn.blit(self.text_btn, (self.text_btn.get_rect(center=(self.width_button/2, self.height_button/2))))
        
        
        

    