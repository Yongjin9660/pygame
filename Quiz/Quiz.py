# Quiz) 하늘에서 떨어지는 동 피하기 게임을 만드시오

# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS 는 30으로 고정

# [게임 이미지]
# 1. 배경 : 640 * 480 (세로 가로) - background.png
# 2. 캐릭터 : 70 * 70 - character.png
# 3. 똥 : 70 * 70 - enemy.png 
import random
import pygame
# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Quiz")

# FPS
clock = pygame.time.Clock()


# 이동 속도
character_speed = 1

# 배경이미지 불러오기
background = pygame.image.load("C:/Users/Yongjin/pygame/Quiz/Image/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/Yongjin/pygame/Quiz/Image/character.png")
character_size = character.get_rect().size      # 이미지의 크기를 구해옴
character_width = character_size[0]         # 캐릭터의 가로 크기
character_height = character_size[1]        # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)    # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0

# 똥 만들기
ddong = pygame.image.load("C:/Users/Yongjin/pygame/Quiz/Image/enemy.png")
ddong_size = ddong.get_rect().size      # 이미지의 크기를 구해옴
ddong_width = ddong_size[0]         # 캐릭터의 가로 크기
ddong_height = ddong_size[1]        # 캐릭터의 세로 크기
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 10

running = True
while running:
    dt = clock.tick(60)     #프레임수
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            running = False            
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_LEFT:  
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:   
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt


    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ddong_y_pos += ddong_speed 

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)
    
    # 충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print("충돌했어요")
        running = False

     # 5. 화면에 그리기
    screen.blit(background, (0, 0))      # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터그리기
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))

    pygame.display.update()             # 게임화면을 다시 그리기!


# 잠시 대기
pygame.time.delay(2000)     # 2초 대기

# pygame 종료
pygame.quit()