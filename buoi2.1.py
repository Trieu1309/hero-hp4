import pygame

pygame.init()

# Create a window of size 800x600
window = pygame.display.set_mode((800, 600))
# Set the window title
pygame.display.set_caption("My First Game")
color="blue"


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.draw.line(window,color, (0, 0), (200, 200), 10)

    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        if color=="blue":
            color="red"
        else:
            color="blue"
    pygame.display.update()
pygame.display.update()