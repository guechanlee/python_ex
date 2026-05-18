# -PC방 자리 관리 프로그램 

# 너는 PC방 사장이다.
# 손님이 자리에 앉으면 "사용중" 으로 바뀌고, 비어있으면 예약할 수 있다.

seats = {
    1: "빈자리",
    2: "사용중",
    3: "빈자리",
    4: "사용중",
    5: "빈자리"
}
# 프로그램 요구사항
# 1.현재 자리 상태를 전부 출력하기
# 2. 사용자에게 원하는 자리 번호 입력받기
# 3.예약할 자리 번호 :
# 4.빈자리라면 "예약 완료" 출력 해당 자리 상태를 "사용중" 으로 변경 이미 사용중이라면 이미 사용중인 자리입니다 출력
# 5.예약 후 전체 자리 상태 다시 출력하기

seats = {
    1: "빈자리",
    2: "사용중",
    3: "빈자리",
    4: "사용중",
    5: "빈자리"
}

for key, value in seats.items():
    print(f'{key}: {value}')

while True:

    userInputData = int(input('예약할 자리 번호: '))


    if seats[userInputData] == '빈자리':
        print('예약 완료')
        break

    else:
        print('이미 사용중인 자리입니다')


    for key, value in seats.items():
        print(f'{key}: {value}')





# - 배달 주문 통계 프로그램 
# 배달 앱에서 하루 주문 데이터를 분석하려고 한다.
# 주어진 주문 목록
orders = [
    "치킨",
    "피자",
    "치킨",
    "햄버거",
    "피자",
    "치킨"
]
# 프로그램 요구사

# 1. 각 음식이 몇 번 주문됐는지 딕셔너리에 저장하기
# 2. 가장 많이 주문된 음식 찾기
# 3. 총 주문 개수 출력하기
# 4. 사용자가 음식 이름 입력하면
# 몇 번 주문됐는지 출력하기

















# count = {}

# for food in orders:
#     if food in count:
#         count[food] += 1
#     else:
#         count[food] = 1

# print('=== 주문 통계 ===')

















# -시험 결과 분석 프로그램 
# 학원에서 시험 결과를 분석하려고 한다.
# 주어진 데이터
# scores = {
#     "민수": 88,
#     "지훈": 72,
#     "수아": 95,
#     "유진": 64,
#     "서연": 100
# }
# 프로그램 요구사항
# 1.전체 학생 점수 출력하기
# 2.평균 점수 계산하기
# 3.최고 점수 학생 찾기
# 4.60점 이상은 합격, 미만은 불합격 출력하기
# 5.90점 이상 학생 수 출력하기
# 6.점수 높은 순으로 학생 출력 도전하기















# import random

# winCount = 0

# while True:

# ranNum = random.randint(1, 3)

# myNum = int(input('1(가위), 2(바위), 3(보) 또는 0(종료)'))

# if myNum == 0:
#     print(f'지금까지 {winCount}번 승리')
#     break

# elif (ranNum == myNum):
#     print('무승부')

# if (ranNum == 1 and myNum == 2) or (ranNum == 2 and myNum == 3) or (ranNum == 3 and myNum == 1):
#     winCount += 1
#     print(f'승리!! 현재{winCount}연승')

# elif (ranNum == 1 and myNum == 3) or (ranNum == 2 and myNum == 1) or (ranNum == 3 and myNum == 2):
#     print('컴퓨터 승')








# seats = {
#     1: '빈자리',
#     2: '사용중',
#     3: '빈자리',
#     4: '사용중',
#     5: '빈자리'
# }

# print("=== 현재 자리 상태 ===")
# for seat, status in seats.item():
#     print(f'{seat}번 자리 : {status}')

# seat_num = int(input('\n예약할 자리 번호 : '))

# if seat_num in seats:
#     if seats[seat_num] == '빈자리':
#         seats[seat_num] = '사용중'
#         print('예약 완료')
#     else:
#         print('이미 사용중인 자리입니다')
# else:
#     print('존재하지 않는 자리입니다.')

# print('\n=== 예약 후 자리 상태 ===')
# for seat, status in seats.item():
#     print(f'{seat}번 자리 : {status}')