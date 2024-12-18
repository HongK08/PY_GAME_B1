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

    import pygame, random, sys
    
    # 색상 목록
    colors = ["red", "green", "blue"]
    
    # Pygame 초기화
    pygame.init()
    
    # 키 반복 설정: 5ms 지연 후 5ms 간격으로 반복
    pygame.key.set_repeat(5, 5)
    
    # 화면 설정: 500x700 크기
    monitor = pygame.display.set_mode((500, 700))
    
    # 랜덤한 색상 선택
    c = random.choice(colors)
    
    # 거북이 이미지 로드
    turtle = pygame.image.load('C:/Temp/turtle.png')
    
    # 거북이 초기 위치 설정
    tx, ty = 200, 300
    
    # 게임 루프
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
                if event.key == pygame.K_SPACE:  # 스페이스바 눌림
                    # 거북이 위치를 랜덤하게 설정
                    tx = random.randint(0, 500)
                    ty = random.randint(0, 700)

#############################################################################

    import turtle  # 거북이 그리기를 위한 라이브러리 import
    import random  # 랜덤 값 생성을 위한 라이브러리 import
    from PIL import Image  # 이미지 처리를 위한 라이브러리 import
    
    # 사용할 색상 목록 정의
    colors = ["red", "green", "blue"]
    
    # 거북이 객체 생성
    t = turtle.Turtle()
    
    # 거북이 모양을 거북이(turtle) 모양으로 설정
    t.shape('turtle')
    
    # 거북이 이동 속도를 최고 속도(0)로 설정
    t.speed(0)
    
    # 거북이 펜을 들고 시작 (선을 그리지 않음)
    t.penup()
    
    # 숫자 1부터 36까지 반복문 수행
    for num in range(1, 37, 1):
        # 거북이를 (0, 0) 위치로 이동
        t.goto(0, 0)
    
        # 거북이를 10도 오른쪽으로 회전
        t.right(10)
    
        # 거북이를 350만큼 앞으로 이동 (선은 그리지 않음)
        t.forward(350)
    
        # 펜 색을 랜덤하게 선택된 색상으로 설정
        t.pencolor(random.choice(colors))
    
        # 숫자 쓰기 (맑은 고딕, 크기 20, 굵게)
        t.write(str(num), font=('맑은고딕', 20, 'bold'))
    
    # 거북이를 다시 (0, 0) 위치로 이동
    t.goto(0, 0)
    
    # 거북이 펜을 내려 시작 (선을 그리도록 설정)
    t.pendown()
    
    # 펜 두께를 5로 설정
    t.pensize(5)
    
    # 각도를 10의 배수로 조정 (10 ~ 360도 범위에서 랜덤 선택)
    angle = random.randint(10, 360) // 10 * 10
    
    # 거북이를 선택된 각도만큼 오른쪽으로 회전
    t.right(angle)
    
    # 거북이를 350만큼 앞으로 이동 (선을 그리면서)
    t.forward(350)
    
    # 숫자 변환 (각도를 10으로 나눈 몫)
    num = angle // 10
    
    # 숫자 형식 만들기 (1의 자리수가 한 자리일 때 앞에 0 추가)
    if num < 10:
        num = '0' + str(num)
    else:
        num = str(num)
    
    # 파일 경로 및 이름 생성
    file = "C:/photo/picture" + num + ".jpg"
    
    # 파일 열기
    img = Image.open(file)
    
    # 이미지 표시
    img.show()
    
    # 거북이 그리기 종료 (창을 닫지 않고 유지하려면 아래 코드 주석 해제)
    # turtle.done()

#############################################################################
#############################################################################
#############################################################################

