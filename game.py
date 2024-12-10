import pygame
import sys
import random
import time
import os

import sys,os




BLACK = (0, 0, 0)
WHITE = (255, 255, 255)  # 점수판 텍스트 색상
padWidth = 1200
padHeight = 1200

EF_list = ['ENM.png', 'ENM1.png', 'ENM2.png', 'ENM3.png']
image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image')

# EFImage 리스트에 절대 경로를 저장
EFImage = [os.path.join(image_dir, file) for file in EF_list]


# 현재 스크립트가 위치한 디렉토리 경로를 구합니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 보스 이미지와 미사일
boss_image = pygame.image.load(os.path.join(current_dir, 'image', 'BOSS.png'))
boss_missile_image = pygame.image.load(os.path.join(current_dir, 'image', 'BOSS_WEP.png'))

# 보스 크기 변경 (크기를 1.5배로 확대)
scaled_boss_image = pygame.transform.scale(boss_image, (int(boss_image.get_width() * 1.5), int(boss_image.get_height() * 1.5)))

# 보스 미사일 크기 변경 (미사일 크기를 0.6배로 축소)
scaled_boss_missile = pygame.transform.scale(boss_missile_image, (int(boss_missile_image.get_width() * 0.6), int(boss_missile_image.get_height() * 0.6)))

# 배경음악 및 효과음 파일 경로
background_music = os.path.join(current_dir, 'sounds', 'back_MS.mp3')
missile_sound = os.path.join(current_dir, 'sounds', 'MIS_LC.mp3')
boss_missile_sound = os.path.join(current_dir, 'sounds', 'spin.mp3')
explosion_sound = os.path.join(current_dir, 'sounds', 'BOOM.mp3')
boss_missile_explosion_sound = os.path.join(current_dir, 'sounds', 'MOI.mp3')

def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x, y))

def drawText(text, x, y, color=(255, 255, 255)):  # 기본 색상은 흰색으로 설정
    font = pygame.font.SysFont("arial", 30)
    textobj = font.render(text, 1, color)
    gamepad.blit(textobj, (x, y))

def drawHealthBar(health, x, y):
    pygame.draw.rect(gamepad, (255, 0, 0), (x, y, 300, 20))  # 배경
    pygame.draw.rect(gamepad, (0, 255, 0), (x, y, (health / 3000) * 300, 20))  # 현재 체력

def initGame():
    global gamepad, clock, background, fighter, missile, explosion
    pygame.init()
    gamepad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption("전투기 게임")

    # 그린 이미지 값 넣기
    background = pygame.image.load(os.path.join(current_dir, 'image', 'ST_BACK.jpg'))
    fighter = pygame.image.load(os.path.join(current_dir, 'image', 'PLA.png'))
    missile = pygame.image.load(os.path.join(current_dir, 'image', 'MISSL.png'))
    explosion = pygame.image.load(os.path.join(current_dir, 'image', 'EXP.png'))
    clock = pygame.time.Clock()

    # 배경음악 로드 및 재생
    pygame.mixer.music.load(background_music)
    pygame.mixer.music.set_volume(0.05)  # 배경음악 볼륨 설정 (50%)
    pygame.mixer.music.play(-1, 0.0)  # 무한 반복으로 배경음악 재생

    # 효과음 로드 및 볼륨 설정
    global missile_fire_sound, boss_missile_fire_sound, explosion_sound, boss_missile_explosion_sound
    missile_fire_sound = pygame.mixer.Sound(missile_sound)
    missile_fire_sound.set_volume(0.04)  # 미사일 발사 소리 볼륨 설정 
    
    boss_missile_fire_sound = pygame.mixer.Sound(boss_missile_sound)
    boss_missile_fire_sound.set_volume(0.1)  # 보스 미사일 발사 소리 볼륨 설정 
    
    explosion_sound = pygame.mixer.Sound(explosion_sound)
    explosion_sound.set_volume(0.01)  # 폭발 소리 볼륨 설정 
    boss_missile_explosion_sound = pygame.mixer.Sound(boss_missile_explosion_sound)
    boss_missile_explosion_sound.set_volume(0.08)  # 보스 미사일 폭발 소리 볼륨 설정 

def runGame():
    global gamepad, clock, background, fighter, missile, explosion
    missileXY = []
    EF_1_passed = 0  # 적기가 통과한 횟수

    # 비행체 SIZE SETUP
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0] // 1.1
    fighterHeight = fighterSize[1] // 1.1
    scaled_fighter = pygame.transform.scale(fighter, (fighterWidth, fighterHeight))

    # 적 비행체 생성기
    EF_1 = pygame.image.load(random.choice(EFImage))
    EF_1Size = EF_1.get_rect().size
    EF_1Width = EF_1Size[0] // 1.1
    EF_1Height = EF_1Size[1] // 1.1
    scaled_EF_1 = pygame.transform.scale(EF_1, (EF_1Width, EF_1Height))

    EF_1X = random.randrange(0, int(padWidth - EF_1Width))
    EF_1Y = 0
    EF_1Speed = random.randint(7, 13)

    # MSL SIZE SETUP
    missileSize = missile.get_rect().size
    missileWidth = missileSize[0] // 0.8
    missileHeight = missileSize[1] // 0.8
    scaled_missile = pygame.transform.scale(missile, (missileWidth, missileHeight))

    # EXP 설정
    explosion_rect = explosion.get_rect()
    scaled_explosion = pygame.transform.scale(explosion, (int(explosion_rect.width * 3), int(explosion_rect.height * 3)))


    # 내 미슬이 적기에 명중했다면 TRUE
    isShot = False
    shotCount = 0

    # 비행체의 Def 위치
    x = padWidth * 0.4
    y = padHeight * 0.6
    fighterX = 0
    fighterY = 0

    # 점수판 표시
    score = 0

    # 보스 관련 설정
    bossAppeared = False
    bossX = padWidth // 2 - 100
    bossY = -150  # 보스를 화면 위에 배치하여 처음에는 보이지 않도록 설정
    bossSpeed = 1  # 보스를 느리게 움직이게 설정
    bossHP = 3000  # 보스 체력 설정
    bossMissiles = []

    # 적기 통과시 게임오버 조건
    maxEnemiesPassed = 10

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                sys.exit()

            # User Input // MOVE KEY INPUT 받기
            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    fighterX -= 18
                elif event.key == pygame.K_RIGHT:
                    fighterX += 18
                elif event.key == pygame.K_UP:
                    fighterY -= 18
                elif event.key == pygame.K_DOWN:
                    fighterY += 18
                elif event.key == pygame.K_SPACE:  # 내 미사일 발사
                    if len(missileXY) < 6:  # 미사일은 6개까지 발사
                        missileX = x + (fighterWidth - missileWidth) // 2
                        missileY = y
                        missileXY.append([missileX, missileY])
                        missile_fire_sound.play()  # 미사일 발사 소리 재생

        if event.type in [pygame.KEYUP]:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                fighterX = 0
                fighterY = 0

        # User Input 이 중단 시 위치의 재 조정
        # X
        x += fighterX
        if x < 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth
        # Y
        y += fighterY
        if y < 0:
            y = 0
        elif y > padHeight - fighterHeight:
            y = padHeight - fighterHeight

        gamepad.fill(BLACK)

        # Draw objects
        drawObject(background, 0, 0)
        drawObject(scaled_fighter, x, y)

        # MSL OUT THE SCREEN
        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -= 10
                missileXY[i][1] = bxy[1]
                # 미슬이 적기에 착탄
                missile_rect = pygame.Rect(bxy[0], bxy[1], missileWidth, missileHeight)

                # 적기의 히트박스를 더 좁혀서 정확한 충돌 판정
                adjusted_EF_1_rect = pygame.Rect(EF_1X + 10, EF_1Y + 10, EF_1Width - 240, EF_1Height - 240)

                if missile_rect.colliderect(adjusted_EF_1_rect):
                    missileXY.remove(bxy)
                    isShot = True
                    shotCount += 1
                    score += 100  # 점수 추가

                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass

        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(scaled_missile, bx, by)

        EF_1Y += EF_1Speed
        # 적기가 나를 지나쳐 간 경우
        if EF_1Y > padHeight:
            EF_1 = pygame.image.load(random.choice(EFImage))
            EF_1Size = EF_1.get_rect().size
            EF_1Width = EF_1Size[0] // 1.1
            EF_1Height = EF_1Size[1] // 1.1
            scaled_EF_1 = pygame.transform.scale(EF_1, (EF_1Width, EF_1Height))
            EF_1X = random.randrange(0, int(padWidth - EF_1Width))
            EF_1Y = 0
            EF_1_passed += 1  # 적기 통과

        # 적기가 10대 통과하면 게임 오버
        if EF_1_passed >= maxEnemiesPassed:
            drawText("GAME OVER!", padWidth // 3, padHeight // 3, (255, 0, 0))  # 게임 오버 텍스트
            drawText(f"Score: {score}", padWidth // 3, padHeight // 2, (255, 255, 255))
            drawText("Press 'Y' to Restart or 'N' to Quit", padWidth // 3, padHeight // 1.8, (255, 255, 255))
            pygame.display.update()
            return  # 게임 종료

        # 보스 관련 동작
        if score >= 3000 and not bossAppeared:
            bossAppeared = True
            bossY = -150  # 보스를 화면 위에 배치하여 처음에는 보이지 않도록 설정

        if bossAppeared:
            # 보스 화면에 등장
            if bossY < 50:
                bossY += 1  # 보스가 느리게 내려옴
            else:
                # 보스 x축으로 기동
                bossX += bossSpeed
                if bossX <= 0 or bossX >= padWidth - scaled_boss_image.get_width():
                    bossSpeed *= -1  # 화면의 끝에 닿으면 방향 전환

            drawObject(scaled_boss_image, bossX, bossY)

            # 보스 미사일 발사 (플레이어를 향한 방향으로)
            if random.randint(1, 150) == 1:  # 발사 확률
                targetX = x + (fighterWidth // 2)  # 플레이어의 x좌표
                targetY = y  # 플레이어의 y좌표
                bossMissiles.append([bossX + 50, bossY + 100, targetX, targetY, time.time()])  # 보스 미사일 초기 위치
                boss_missile_fire_sound.play()  # 보스 미사일 발사 소리 재생

            # 보스 미사일 이동 및 충돌 처리
            for i, (bx, by, tx, ty, start_time) in enumerate(bossMissiles):
                dx = tx - bx
                dy = ty - by
                distance = (dx ** 2 + dy ** 2) ** 0.5
                move_x = (dx / distance) * 5  # 이동 속도 설정
                move_y = (dy / distance) * 5
                bx += move_x
                by += move_y
                bossMissiles[i] = [bx, by, tx, ty, start_time]

                # 미사일이 화면 밖으로 나가면 리스트에서 제거
                if by > padHeight:
                    bossMissiles.pop(i)

                # 보스 미사일이 낙하 후 자폭 처리 (2초 후)
                if time.time() - start_time >= 5:
                    # 자폭 처리 (미사일이 사라짐)
                    bossMissiles.pop(i)
                    boss_missile_explosion_sound.play()  # 자폭 소리 재생

                missile_rect = pygame.Rect(bx, by, scaled_boss_missile.get_width(), scaled_boss_missile.get_height())
                player_rect = pygame.Rect(x + 10, y + 10, fighterWidth - 20, fighterHeight - 20)  # 좁힌 플레이어 충돌 박스
                if missile_rect.colliderect(player_rect):
                    drawText("GAME OVER!", padWidth // 3, padHeight // 3, (255, 0, 0))  # 게임 오버 텍스트
                    drawText(f"Score: {score}", padWidth // 3, padHeight // 2, (255, 255, 255))
                    pygame.display.update()
                    pygame.time.wait(3000)
                    return  # 게임 종료

                drawObject(scaled_boss_missile, bx, by)  # 보스 미사일 그리기

        # 보스 체력 감소 처리
        if isShot and bossAppeared:
            bossHP -= 50  
            if bossHP <= 0:
                drawText("BOSS DEFEATED!", padWidth // 3, padHeight // 3, (255, 0, 0))
                drawText("GAME CLEAR!", padWidth // 3, padHeight // 2, (255, 0, 0))  # 게임 클리어 텍스트
                drawText("You Win!", padWidth // 3, padHeight // 1.8, (255, 255, 255))  # 승리 텍스트
                pygame.display.update()
                pygame.time.wait(2000)
                return  # 게임 종료

        # 보스 체력 게이지 표시
        if bossAppeared:
            drawHealthBar(bossHP, padWidth - 320, 10)

        # 적기 그리기
        drawObject(scaled_EF_1, EF_1X, EF_1Y)

        # 미사일이 맞은 경우
        if isShot:
            # 폭발 이미지 그리기
            drawObject(scaled_explosion, EF_1X, EF_1Y)
            explosion_sound.play()  # 폭발 소리 재생
            # 그리고 다시 튀어나오기
            EF_1 = pygame.image.load(random.choice(EFImage))
            EF_1Size = EF_1.get_rect().size
            EF_1Width = EF_1Size[0] // 1.1
            EF_1Height = EF_1Size[1] // 1.1
            scaled_EF_1 = pygame.transform.scale(EF_1, (EF_1Width, EF_1Height))
            EF_1X = random.randrange(0, int(padWidth - EF_1Width))
            EF_1Y = 0
            isShot = False

        # 점수판과 적기 통과 표시
        drawText(f"Score: {score}", 10, 10)
        drawText(f"Enemies Passed: {EF_1_passed}", 10, 40)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


initGame()
runGame()
