# 1. 파이게임 모듈을 불러온다.
import pygame

# 2. 초기화 시킨다.
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# 3. 이미지를 가져온다.
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

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

    screen.blit(player, (100,100))


    # 7. 화면을 다시 그린다.
    pygame.display.flip()

    # 8. 게임을 종료
    for event in pygame.event.get():
        # X 를 눌렀으면,
        if event.type == pygame.QUIT:
            # 게임종료한다
            pygame.quit()
            exit(0)
