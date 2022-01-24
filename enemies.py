import pygame 
import random


pygame.init()

class Enemies:
    def __init__(self):
        self.sprites_meteors = []
        self.sprites_meteors.append(pygame.image.load("./assets/meteors/Meteor_01.png").convert_alpha())
        self.sprites_meteors.append(pygame.image.load("./assets/meteors/Meteor_02.png").convert_alpha())
        self.sprites_meteors.append(pygame.image.load("./assets/meteors/Meteor_03.png").convert_alpha())
        self.sprites_meteors.append(pygame.image.load("./assets/meteors/Meteor_04.png").convert_alpha())
        self.sprites_meteors.append(pygame.image.load("./assets/meteors/Meteor_05.png").convert_alpha())
        self.sprites_meteors.append(pygame.image.load("./assets/meteors/Meteor_06.png").convert_alpha())
        self.sprites_meteors.append(pygame.image.load("./assets/meteors/Meteor_07.png").convert_alpha())
        self.sprites_meteors.append(pygame.image.load("./assets/meteors/Meteor_08.png").convert_alpha())
        self.sprites_meteors.append(pygame.image.load("./assets/meteors/Meteor_09.png").convert_alpha())
        self.sprites_meteors.append(pygame.image.load("./assets/meteors/Meteor_10.png").convert_alpha())
        self.rect_list = []
        
        
        self.entities = []
        self.nb_entities = 0
        self.meteor = pygame.transform.scale(self.sprites_meteors[0] ,(50,50)) 
        
    def drawEnemies(self, surface : pygame.surface.Surface):
        if self.nb_entities < 10 :
            rand = random.randint(30, surface.get_size()[0]-30)
            rand_meteor = random.randint(1, 6)
            rand_velocity = random.randint(5, 10)
            self.nb_entities += 1
            self. meteor = pygame.transform.scale(self.sprites_meteors[rand_meteor], (50,50)) 
            
            self.entities.append({"meteor" : self.meteor, "x" : rand, "y" : 10, "velocity" : rand_velocity, "rect": self.meteor})
    
        for entitie in self.entities:
            #Draw to surface 
            surface.blit(entitie["meteor"], (entitie["x"],entitie["y"]), entitie["meteor"].get_rect())
            entitie["y"] += entitie["velocity"]
            self.rect_list.append(self.meteor.get_rect())
            if entitie["y"] >= surface.get_size()[1]:
                
                self.entities.remove(entitie)
                self.nb_entities -= 1
                
              
    def get_entities_pos(self):
        return self.entities