import pygame
pygame.init()

win = pygame.display.set_mode((600, 400))

pygame.display.set_caption("AVoid Python Edition")

playerX = 280
playerY = 300
playerWH = 40
enemyWH = 40
enemyX = playerX
enemyY = 50
canMoveRight = True
canMoveLeft = True
vel = 2

FPS = 360
fpsClock = pygame.time.Clock()

run = True
while run:
    
    enemyX = playerX

    fpsClock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and playerX > vel:
        playerX -= vel
    elif playerX < 600 - playerWH - vel:
        playerX += vel

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), (playerX, playerY, playerWH, playerWH))
    pygame.draw.rect(win, (255, 255, 255), (enemyX, enemyY, enemyWH, enemyWH))
    
    
    pygame.display.update()
    



pygame.quit()