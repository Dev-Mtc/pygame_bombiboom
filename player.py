import pygame

#Player starting position
X_POS = 500
Y_POS = 600



class Player(pygame.sprite.Sprite):
    
    def __init__(self) : 
        super().__init__()
        self.is_alive = True
        self.healh = 100
        self.shield = 100
        self.x_pos = X_POS
        self.y_pos = Y_POS
        self.vel_y = 5
        self.animations = { "running" : False, "jumping" : False, "attacking" : False}
        self.last_side = {"left" : False, "right" : False}
        
        
        ###
        # loading movement sprites
        ###
        self.sprites_character = []
        self.sprites_character.append(pygame.image.load("./assets/character_move/0_Warrior_Idle_000.png"))
        self.sprites_character.append(pygame.image.load("./assets/character_move/0_Warrior_Run_000.png"))
        self.sprites_character.append(pygame.image.load("./assets/character_move/0_Warrior_Run_004.png"))
        self.sprites_character.append(pygame.image.load("./assets/character_move/0_Warrior_Run_005.png"))
        self.sprites_character.append(pygame.image.load("./assets/character_move/0_Warrior_Run_009.png"))
        self.sprites_character.append(pygame.image.load("./assets/character_move/0_Warrior_Run_010.png"))    
        self.sprites_character.append(pygame.image.load("./assets/character_move/0_Warrior_Run_014.png"))    
        self.sprites_character.append(pygame.image.load("./assets/character_move/0_Warrior_Run_015.png"))
        self.sprites_character.append(pygame.image.load("./assets/character_move/0_Warrior_Run_016.png"))
        self.sprites_character.append(pygame.image.load("./assets/character_move/0_Warrior_Run_017.png"))
        self.sprites_character.append(pygame.image.load("./assets/character_move/0_Warrior_Run_018.png"))
        self.sprites_character.append(pygame.image.load("./assets/character_move/0_Warrior_Run_019.png"))   
        self.sprites_character.append(pygame.image.load("./assets/character_move/0_Warrior_Idle_020.png"))
        
           
        self.sprite_states_left = 0
        self.sprite_states_right = 7
        
        ###
        # Loading attacks sprites
        ###
        self.sprites_attacks = []
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Left_Warrior_Attack_2_000.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Left_Warrior_Attack_2_001.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Left_Warrior_Attack_2_002.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Left_Warrior_Attack_2_003.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Left_Warrior_Attack_2_004.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Left_Warrior_Attack_2_007.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Left_Warrior_Attack_2_008.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Left_Warrior_Attack_2_009.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Left_Warrior_Attack_2_010.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Left_Warrior_Attack_2_011.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Left_Warrior_Attack_2_014.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Right_Warrior_Attack_2_000.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Right_Warrior_Attack_2_001.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Right_Warrior_Attack_2_002.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Right_Warrior_Attack_2_003.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Right_Warrior_Attack_2_004.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Right_Warrior_Attack_2_005.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Right_Warrior_Attack_2_006.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Right_Warrior_Attack_2_007.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Right_Warrior_Attack_2_008.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Right_Warrior_Attack_2_009.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Right_Warrior_Attack_2_010.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Right_Warrior_Attack_2_011.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Right_Warrior_Attack_2_012.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Right_Warrior_Attack_2_013.png"))
        self.sprites_attacks.append(pygame.image.load("./assets/character_attacks/Right_Warrior_Attack_2_014.png"))
        
        self.sprite_attack_left_state = 0
        self.sprite_attack_right_state = 10
        
     
        self.image = pygame.transform.scale(self.sprites_character[self.sprite_states_left], (150,150))
        self.rect = self.image.get_rect()
        
        
    #
    # Manage movement
    # 
    def move_right(self, velocity):
        self.animations["running"] = True
        self.last_side["left"] = False
        self.last_side["right"] = True
        self.x_pos += velocity
        if self.sprite_states_right >= 11 :
            self.sprite_states_right = 7
        self.sprite_states_right += 1 
        self.image = pygame.transform.scale(self.sprites_character[self.sprite_states_right], (150,150))
        
    def move_left(self, velocity):
        self.animations["running"] = True
        self.last_side["left"] = True
        self.last_side["right"] = False
        self.x_pos -= velocity
        if self.sprite_states_left >= 6 :
            self.sprite_states_left = 1
        self.sprite_states_left += 1 
        self.image = pygame.transform.scale(self.sprites_character[self.sprite_states_left], (150,150))
                
    def jump(self):
        self.y_pos -= self.vel_y*4
        self.vel_y -= 1
        if self.vel_y < -5:
            self.vel_y = 5
            self.animations["jumping"] = False
            
    def get_jump_state(self):
        return self.animations["jumping"]     
    def set_jump_state(self, state : bool):
        self.animations["jumping"] = state

    
    #
    # Manage attacks
    #   
    def get_healh(self): 
        return self.healh
    def set_damage(self):
        if self.healh > 0:
            self.healh -= 1
        else :
            self.is_alive = False
    def get_shield(self): 
        return self.shield

            
    def attack(self, surface : pygame.surface.Surface):
        self.animations["attacking"] = True
        
        self.image = pygame.transform.scale(self.sprites_attacks[5], (150,150)) 

        
    
    
    #
    # Draw update player 
    #        
    def draw_player(self, surface : pygame.surface.Surface):
        surface.blit(self.image,(self.x_pos,self.y_pos))
        pygame.draw.circle(surface, (255,255,255), (self.x_pos + 75, self.y_pos +75) , 150, 1 , draw_top_left=True , draw_top_right=True)   
        
        
    def update_animation(self):
        if self.animations["running"] == True :
            if self.last_side["left"] == True and self.last_side["right"] == False :
                self.image = pygame.transform.scale(self.sprites_character[0], (150,150))
            elif self.last_side["left"] == False and self.last_side["right"] == True:
                self.image = pygame.transform.scale(self.sprites_character[12], (150,150))
            self.sprite_states_left = 1
            self.sprite_states_right = 7
            self.animations["running"] = False
        
