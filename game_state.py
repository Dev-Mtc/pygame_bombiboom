import pygame

pygame.init()

class GameState: 
    def __init__(self) :
        self.state = "lobby"
        self.screen = pygame.display.set_mode((1500, 800))
        self.running = True
  
        
    def get_state(self):
        return self.state
    
    def handle_event(self) :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False    
    
    def run(self):
        while self.running:             
            self.clock.tick(60)
            self.handle_event()
            pygame.display.flip()