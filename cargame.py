import pygame
import random

width=800
height=600

BLACK=(0,0,0)
WHITE=(255,255,255)
GREY=(128,128,128)

RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

LIST_COLOR=[RED,GREEN,BLUE]

class player:
    def __init__(self,x,y,w,h):
        self.x-x
        self.y=y
        self.w=w
        self.h=h
    def draw(self,screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.w, self.h))
            
    def move(self,dx,dy,boundaries):
        dx=max(boundaries[0],min(self.x+dx,boundaries[1]-self.width))
        dy=max(0,min(self.y+dy,boundaries[2]-self.height))

        self.x=dx
        self.y=dy
    
class obstacle: 
    def __init__(self,x,y,w,h,speed):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.speed=speed
        
        self.color=random.choice(LIST_COLOR)
    def draw(self,screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
    def move(self):
        self.y+=self.speed
        
class UI:
    def draw_game_info(self,screen,score,lives,speed,x,y):
        font=pygame.font.Font('freesansbold.ttf', 32)
        redered_text=font.render(f'Score: {score} | Lives: {lives} | Speed: {speed}', True, WHITE)
        text_rect=redered_text.get_rect(center=(x,y))
        screen.blit(redered_text, text_rect)     

class gamemanager:
    def __init__(self):
        pygame.init()
        self.w=800
        self.h=600
        self.screen=pygame.display.set_mode((width,height))
        self.clock=pygame.time.Clock()
        
        self.running=True
        self.score=0
        self.lives=3