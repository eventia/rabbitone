# 08. 화살에 맞은 적 소멸
#
# 파이게임 참고 문서들 http://www.pygame.org/docs/
# 1 - 파이게임 모듈을 가져온다
import pygame
import math
import random

# 2 - 초기화 시킨다
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))  # 게임창을 만든다
keys = [False, False, False, False]
playerpos = [100,100]
acc = [0,0]
arrows = []
badtimer=100
badtimer1=0
badguys=[[640,100],]
healthvalue=194

# 3.이미지를 가져온다
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")
badguyimg1 = pygame.image.load("resources/images/badguy.png")
badguyimg = badguyimg1


# 4 - 계속 화면이 보이도록 반복해서 실행한다
while True:
    badtimer = badtimer-1

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

    # 6.1 - 플레이어 포지션과 회전
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width//2, playerpos[1]-playerrot.get_rect().height//2)
    screen.blit(playerrot, playerpos1)

    # 6.2 - 화살 그리기
    for bullet in arrows:
        index=0
        velx = math.cos(bullet[0])*10
        vely = math.sin(bullet[0])*10
        bullet[1] = bullet[1]+velx
        bullet[2] = bullet[2]+vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index = index+1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))

    # 6.3 - 오소리 공격
    if badtimer == 0:
        badguys.append([640, random.randint(50,430)])
        badtimer = 100-(badtimer1*2)
        if badtimer1 >= 35:
            badtimer1 = 35
        else:
            badtimer1 = badtimer1+5
    index=0
    for badguy in badguys:
        if badguy[0] < -64:
            badguys.pop(index)
        badguy[0] = badguy[0]-7

        # 6.3.1 - 성 공격
        badrect = pygame.Rect(badguyimg.get_rect())
        badrect.top = badguy[1]
        badrect.left = badguy[0]
        if badrect.left < 64:
            healthvalue = healthvalue-random.randint(5,20)
            badguys.pop(index)

        #6.3.2 - 충돌 체크
        index1 = 0
        for bullet in arrows:
            bullrect = pygame.Rect(arrow.get_rect())
            bullrect.left = bullet[1]
            bullrect.top = bullet[2]
            if badrect.colliderect(bullrect):
                acc[0] = acc[0]+1
                badguys.pop(index)
                arrows.pop(index1)
            index1 = index1+1

        index = index+1
    for badguy in badguys:
        screen.blit(badguyimg, badguy)

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

        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            acc[1] = acc[1]+1
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32), \
                position[0]-(playerpos1[0]+26)),playerpos1[0]+32,\
                playerpos1[1]+32])

    # 9 - 플레이어 움직이기
    if keys[0]:
        playerpos[1] = playerpos[1] - 5
    elif keys[2]:
        playerpos[1] = playerpos[1] + 5
    if keys[1]:
        playerpos[0] = playerpos[0] - 5
    elif keys[3]:
        playerpos[0] = playerpos[0] + 5
