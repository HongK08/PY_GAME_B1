# PY_GAME_B1

    import random  # 랜덤 모듈 임포트 (무작위 수 생성)

    number = random.randint(1, 99)  # 1부터 99까지의 임의의 정수 생성
    if number < 10:  # 숫자가 10보다 작으면
        number = '0' + str(number)  # 숫자 앞에 '0' 추가 (예: 5 -> 05)
    else:
        number = str(number)  # 그 외에는 문자열로 변환
    
    #파일 이름 생성
    filename = "C:/photo/picture" + number + ".jpg"
    print(f"읽을 파일: {filename}")  # 읽을 파일 경로 출력
    
    #이미지 열기
    try:
        img = Image.open(filename)
        print(f"이미지 열기 성공!")  # 이미지 열기 성공 메시지
    except FileNotFoundError:
        print(f"오류: 파일 '{filename}'을(를) 찾을 수 없습니다.")  # 파일 못 찾을 시 에러 메시지
    
    else:  # 이미지 열기 성공 시 실행
        # 이미지 변형
        img = img.transpose(Image.FLIP_LEFT_RIGHT)  # 이미지 좌우 반전
        img.show()
    
        img = img.transpose(Image.FLIP_TOP_BOTTOM)  # 이미지 상하 반전
        img.show()
    
        img = img.rotate(45, expand=True)  # 이미지 45도 회전 (expand=True: 빈 공간 채움)
        img.show()
    
        img = img.filter(ImageFilter.CONTOUR)  # 이미지 윤곽선 필터 적용
        img.show()
    
        # 결과 이미지 저장
        filename = "C:/photo/output" + number + ".jpg"
        print(f"저장할 파일: {filename}")  # 저장할 파일 경로 출력
        img.save(filename)
        print(f"이미지 저장 성공!")  # 이미지 저장 성공 메시지

###############################################################################
        
    import pygame, random, sys  # 필요한 모듈 임포트
    colors = ["red", "green", "blue"]  # 색상 리스트
    
    pygame.init()  # Pygame 초기화
    monitor = pygame.display.set_mode((500, 700))  # 화면 크기 설정
    
    while True:
        c = random.choice(colors)  # 색상 리스트에서 랜덤으로 색상 선택
        monitor.fill(c)  # 화면을 선택한 색상으로 채움
        pygame.display.update()  # 화면 업데이트
        print("#", end="")  # '#' 출력 (프로그레스 표시용)
        
#############################################################################

    import pygame, random, sys  # 필요한 모듈 임포트
    
    colors = ["red", "green", "blue"]  # 색상 리스트
    
    pygame.init()  # Pygame 초기화
    monitor = pygame.display.set_mode((500, 700))  # 화면 크기 설정
    c = random.choice(colors)  # 랜덤 색상 선택
    turtle = pygame.image.load('C:/Temp/turtle.png')  # 거북이 이미지 로드
    
    while True:
        monitor.fill(c)  # 화면을 선택한 색상으로 채움
        monitor.blit(turtle, (200, 300))  # 거북이 이미지를 (200, 300) 좌표에 그리기
        pygame.display.update()  # 화면 업데이트
    
        for event in pygame.event.get():  # 이벤트 처리 루프
            if event.type == pygame.QUIT:  # 종료 이벤트 처리
                pygame.quit()  # Pygame 종료
                sys.exit()  # 프로그램 종료

#############################################################################

 import pygame, random, sys

#색상 목록
colors = ["red", "green", "blue"]

#Pygame 초기화
pygame.init()

#키 반복 설정: 5ms 지연 후 5ms 간격으로 반복
pygame.key.set_repeat(5, 5)

#화면 설정: 500x700 크기
monitor = pygame.display.set_mode((500, 700))

#랜덤한 색상 선택
c = random.choice(colors)

#거북이 이미지 로드
turtle = pygame.image.load('C:/Temp/turtle.png')

#거북이 초기 위치 설정
tx, ty = 200, 300

#게임 루프
while True:
    # 화면 채우기
    monitor.fill(c)

    # 거북이 그리기
    monitor.blit(turtle, (tx, ty))

    # 화면 업데이트
    pygame.display.update()

    # 이벤트 처리
    for event in pygame.event.get():
        # 창 닫기 이벤트
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 키보드 입력 이벤트
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # 왼쪽 화살표
                tx -= 5  # 거북이 왼쪽으로 이동
            elif event.key == pygame.K_RIGHT:  # 오른쪽 화살표
                tx += 5  # 거북이 오른쪽으로 이동
            elif event.key == pygame.K_UP:  # 위쪽 화살표
                ty -= 5  # 거북이 위로 이동
            elif event.key == pygame.K_DOWN:  # 아래쪽 화살표
                ty += 5  # 거북이 아래로 이동

#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################

