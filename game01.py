# 01. 게임화면 초기화
#
# 1 - 파이게임 모듈을 가져온다
# 모듈을 사용하기전 모듈을 설치해야 한다.
# pip install pygame

import pygame

# 2 - 초기화 시킨다
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))  # 게임창을 만든다
# help(pygame.display.set_mode)
# 윈도우(스크린)의 크기와 해상도를 초기화해준다.
#
# help(screen)
# screen 이 Surface 클래스의 객체라는 것을 알 수 있음
# Surface 클래스에 fill() 메소드를 확인

# 3.이미지를 가져온다


# 4 - 계속 화면이 보이도록 반복해서 실행한다
while True:

    # 5 - 화면을 깨끗하게 청소한다 (R,G,B) 값 사용
    screen.fill((0,0,0))

    # 6. - 모든 요소들을 다시 그린다


    # 7. - 화면을 다시 그린다
    pygame.display.flip()
	# flip() 은 화면 전체를 업데이트한다.

    # 8 - 게임을 종료할 준비, 종료아이콘(x)를 누르면 종료되도록 프로그램
    for event in pygame.event.get():
        # X 를 눌렀는지 검사
        if event.type==pygame.QUIT:
            # 게임종료
            pygame.quit()
            exit(0)
