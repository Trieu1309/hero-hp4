import pygame


pygame.init()

display=pygame.display.set_mode((800,600))
pygame.display.set_caption("My Game")

icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)


pygame.draw.rect(display,"#ff0000",pygame.Rect(0,0,500,500))
pygame.draw.rect(display,"blue",pygame.Rect(50,50,400,400))
pygame.draw.rect(display,"green",pygame.Rect(100,100,300,300))
pygame.draw.rect(display,"pink",pygame.Rect(150,150,200,200))
pygame.draw.rect(display,"yellow",pygame.Rect(200,200,100,100))









pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.update()