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
