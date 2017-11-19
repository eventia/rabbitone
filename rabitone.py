# 1. 파이게임 모듈을 불러온다.
import pygame
import math

# 2. 초기화 시킨다.
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# 3. 이미지를 가져온다.
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

keys = [False, False, False, False]
playpos = [100,100]


# 4. 계속 화면이 보이도록 한다.

while True:
    # 5. 화면을 깨끗하게 한다.
    screen.fill((0,0,0))   # (R,G,B)

    # 6. 모든 요소들을 다시 그린다.
    for x in range(width//grass.get_width()+1):
        for y in range(height//grass.get_height()+1):
            screen.blit(grass, (x*100,y*100))

    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))

    # 6.1 - Set player position and rotaion
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playpos[1]+32), position[0]-(playpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playpos[0]-playerrot.get_rect().width//2, playpos[1]-playerrot.get_rect().height//2)
    screen.blit(playerrot,playerpos1)


    # 7. 화면을 다시 그린다.
    pygame.display.flip()

    # 8. 게임을 종료
    for event in pygame.event.get():
        # X 를 눌렀으면,
        if event.type == pygame.QUIT:
            # 게임종료한다
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0] = True
            elif event.key == pygame.K_a:
                keys[1] = True
            elif event.key == pygame.K_s:
                keys[2] = True
            elif event.key == pygame.K_d:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False

    # 9 - Move player
    if keys[0]:
        playpos[1] = playpos[1] - 5
    elif keys[2]:
        playpos[1] = playpos[1] + 5
    elif keys[1]:
        playpos[0] = playpos[0] - 5
    elif keys[3]:
        playpos[0] = playpos[0] + 5
