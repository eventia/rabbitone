# 04. 키보드로 그림 움직이기
#
# 파이게임 참고 문서들 http://www.pygame.org/docs/
# 1 - 파이게임 모듈을 가져온다
import pygame

# 2 - 초기화 시킨다
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))  # 게임창을 만든다

# 3.이미지를 가져온다
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
keys = [False, False, False, False]
playerpos = [100,100]

# 4 - 계속 화면이 보이도록 반복해서 실행한다
while True:

    # 5 - 화면을 깨끗하게 청소한다 (R,G,B) 값 사용
    screen.fill((0,0,0))

    # 6. - 모든 요소들을 다시 그린다
    for x in range(width//grass.get_width()+1):
        for y in range(height//grass.get_height()+1):
            screen.blit(grass,(x*100,y*100))
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345))
    screen.blit(player, playerpos)

    # 7. - 화면을 다시 그린다
    pygame.display.flip()

    # 8 - 게임을 종료할 준비, 종료아이콘(x)를 누르면 종료되도록 프로그램
    for event in pygame.event.get():
        # X 를 눌렀는지 검사
        if event.type==pygame.QUIT:
            # 게임종료
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_w:
                keys[0]=True
            elif event.key==pygame.K_a:
                keys[1]=True
            elif event.key==pygame.K_s:
                keys[2]=True
            elif event.key==pygame.K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False

    # 9 - Move player
    if keys[0]:
        playerpos[1] = playerpos[1] - 5
    elif keys[2]:
        playerpos[1] = playerpos[1] + 5
    if keys[1]:
        playerpos[0] = playerpos[0] - 5
    elif keys[3]:
        playerpos[0] = playerpos[0] + 5
