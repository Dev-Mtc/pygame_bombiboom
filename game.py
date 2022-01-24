import pygame 
from player import Player
from interface import *
from enemies import Enemies


#Widht height of the screen 
WIDTH = 1200
HEIGHT = 800


class game: 
    
    def __init__(self) :
        pygame.init()
        self.running_game = False
        self.running_menu = False
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("BombiBoom")
        self.clock = pygame.time.Clock()
        self.bg_game = pygame.image.load("./assets/bg-main.png")
        self.img_game = pygame.transform.scale(self.bg_game,self.screen.get_size())
        self.bg_menu = pygame.image.load("./assets/bg-menu.jpg")
        self.img_menu = pygame.transform.scale(self.bg_menu,self.screen.get_size())
        self.screen.blit(self.bg_menu, (0,0))
        self.player = Player(self.screen)
        self.pressed_key = {}
        self.interface = Interface()
        self.enemies = Enemies()
    #
    # Event handler 
    # 
    def handle_event(self) :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running_game = False 
                self.running_menu = False
            elif event.type == pygame.KEYDOWN:
                self.pressed_key[event.key] = True
            elif event.type == pygame.KEYUP:
                self.pressed_key[event.key] = False
                # Check if we can stop animation and reset sprite 
                self.player.update_animation()
        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 :
                    self.player.attack(self.screen)    
            
                
                
    def userInput(self):
        if self.pressed_key.get(pygame.K_d) and self.player.x_pos + 150 < self.screen.get_size()[0]: 
            self.player.move_right(8)
        elif self.pressed_key.get(pygame.K_q) and self.player.x_pos > 0  :
            self.player.move_left(8)
            self.check_colision()
        elif self.pressed_key.get(pygame.K_SPACE) and self.player.get_jump_state() == False:
            self.player.set_jump_state(True)
            self.player.jump()
            
    def check_colision(self):
        entities = self.enemies.get_entities_pos()
        
    #
    # Main loop of the game
    # 
    def run_game(self):
        self.running_game = True
        while self.running_game:             
            self.clock.tick(60)
            self.screen.blit(self.img_game, (0,0))
            self.player.draw_player(self.screen)
            self.interface.draw_heal_bar(self.player.get_healh(), self.screen)
            self.interface.draw_shield_bar(self.player.get_shield(), self.screen)
            self.enemies.drawEnemies(self.screen)
            self.handle_event()
            self.userInput()
            pygame.display.flip()
     
    def run_menu(self):
        self.running_menu = True
        while self.running_menu == True: 
            self.screen.blit(self.img_menu, (0,0))
            self.button_play = Button((self.screen.get_size()[0]/2)-100,(self.screen.get_size()[1]/2)-50, 200, 50, "Play", 27, (255,255,255), (62,172,47))
            self.button_exit = Button((self.screen.get_size()[0]/2)-100,(self.screen.get_size()[1]/2+70)-50, 200, 50, "Exit", 27,(255,255,255), (62,172,47))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running_game = False 
                    self.running_menu = False
                    
            mouse_pressed = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
        
            
            self.button_play.is_hovering(mouse_pos) 
            self.button_exit.is_hovering(mouse_pos) 
            
            if self.button_play.is_pressed(mouse_pos, mouse_pressed):  
                self.run_game() 
                self.running_menu = False
     
            self.screen.blit(self.button_play.rect_btn, self.button_play.rect)
            self.screen.blit(self.button_exit.rect_btn, self.button_exit.rect)
            self.clock.tick(60)
         
            pygame.display.flip()