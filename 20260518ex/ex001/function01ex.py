# goods = {
#     '새우깡': 1200,
#     '비비빅': 400,
#     '초코파이': 500,
#     '맛동산': 1500,
# }

# totalPrice = 0

# def shrimpCrackerPrice():
#     global totalPrice
#     totalPrice += goods['새우깡'] * shrimpCrackers
#     print(f'새우깡 구매 금액: {goods['새우깡'] * shrimpCrackers}원')

# def bibibigPrice():
#     global totalPrice
#     totalPrice += goods['비비빅'] * bibibigs
#     print(f'비비빅 구매 금액: {goods['비비빅'] * bibibigs}원')

# def chocopiPrice():
#     global totalPrice
#     totalPrice += goods['초코파이'] * chocopis
#     print(f'초코파이 구매 금액: {goods['초코파이'] * chocopis}원')

# def matdongsanPrice():
#     global totalPrice
#     totalPrice += goods['맛동산'] * matdongsans
#     print(f'맛동산 구매 금액: {goods['맛동산'] * matdongsans}원')


# shrimpCrackers = int(input('새우깡 구매 개수: '))
# bibibigs = int(input('비비빅 구매 개수: '))
# chocopis = int(input('초코파이 구매 개수: '))
# matdongsans = int(input('맛동산 구매 개수: '))

# print(f'새우깡 구매 개수: {shrimpCrackers}')
# print(f'비비빅 구매 개수: {bibibigs}')
# print(f'초코파이 구매 개수: {chocopis}')
# print(f'맛동산 구매 개수: {matdongsans}')
# print('=' * 40)
# shrimpCrackerPrice()
# bibibigPrice()
# chocopiPrice()
# matdongsanPrice()
# print('=' * 40)
# print(f'총 구매 금액: {totalPrice}')
# print('=' * 40)

# 전역 변수(global variable)
# 다 사용 가능

# 지역 변수(local variable)
# 조건문: 클론 뒤에 쓰는 변수

# 함수 내부에 같은 이름의 변수가 있으면
# 지역 변수가 우선이다.

# global이란
# 함수 내부에서 전역변수를 수정하고 싶을 떄 사용합니다.


# # global count

# count = 0

# def alal():
#     global count
#     count += 1
#     print(count)

# alal()

# nameList = ['철수','영희','기훈']


# for i, name in enumerate(nameList):
#     print('{}: {}'.format(i + 1, name))


# student = {
#     '이름': '홍길동',
#     '나이': 25
# }

# print(f'나이: {student['나이']}')

# def modifyStudentAge():
#     student['나이'] += 1

# modifyStudentAge()
# print(f'나이: {student['나이']}')

def print_round(number):
    print(round(number))
    
print_round(4.6)
print_round(2.2)
