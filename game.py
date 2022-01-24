import pygame 
from player import Player
from interface import Interface
from enemies import Enemies


#Widht height of the screen 
WIDTH = 1200
HEIGHT = 800


class game: 
    
    def __init__(self) :
        pygame.init()
        self.running = True
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("BombiBoom")
        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load("./assets/bg-main.png")
        self.img = pygame.transform.scale(self.bg,self.screen.get_size())
        self.screen.blit(self.bg, (0,0))
        self.player = Player(self.screen)
        self.pressed = {}
        self.interface = Interface()
        self.enemies = Enemies()
    #
    # Event handler 
    # 
    def handle_event(self) :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False 
            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False
                # Check if we can stop animation and reset sprite 
                self.player.update_animation()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 :
                    self.player.attack(self.screen)    
            
                
                
    def userInput(self):
        if self.pressed.get(pygame.K_d) and self.player.x_pos + 150 < self.screen.get_size()[0]: 
            self.player.move_right(8)
        elif self.pressed.get(pygame.K_q) and self.player.x_pos > 0  :
            self.player.move_left(8)
            self.check_colision()
        elif self.pressed.get(pygame.K_SPACE) and self.player.get_jump_state() == False:
            self.player.set_jump_state(True)
            self.player.jump()
            
    def check_colision(self):
        entities = self.enemies.get_entities_pos()
        
    #
    # Main loop of the game
    # 
    def run(self):
        while self.running:             
            self.clock.tick(60)
            self.screen.blit(self.img, (0,0))
            self.player.draw_player(self.screen)
            self.interface.draw_heal_bar(self.player.get_healh(), self.screen)
            self.interface.draw_shield_bar(self.player.get_shield(), self.screen)
            self.enemies.drawEnemies(self.screen)
            self.handle_event()
            self.userInput()
            pygame.display.flip()
     

