# 자주 사용하는 모듈: 내장 모듈
# 이러한 내장 모듈들은 절대로 외우는 것이 아니다
# 따라서 가볍게 흝어보고 필요할 때 찾아서 사용하면 됩니다.

# math 모듈: 수학 함수와 관련된 모듈
'''
fabs(): 절댓값을 반환
ceil(): 소수점 이하 올림한 값을 반환
floor(): 소수점 이하 내림한 값을 반환
trunc(): 소수점 이하 버림한 값을 반환
gcd(): 최대공약수를 반환
factorial(): 팩토리얼한 값을 반환
sqrt(): 제곱근을 반환
'''

import math

print(f'math.fabs(-3.1415): {math.fabs(-3.1415)}') # 절댓값
print(f'math.ceil(-3.1415): {math.ceil(-3.1415)}') # 올림
print(f'math.floor(-3.1415): {math.floor(-3.1415)}') # 내림
print(f'math.trunc(-3.1415): {math.trunc(-3.1415)}') # 버림
print(f'math.gcd(9, 21): {math.gcd(9, 21)}') # 최대공약수
print(f'math.factorial(7): {math.factorial(7)}') # 팩토리얼
print(f'math.sqrt(9): {math.sqrt(9)}') # 제곱근

# 파이썬 내장 함수 중에서 수학과 관련한 함수
'''
sum(): 전체 합을 반환
max(): 최댓갑을 반환
min(): 최솟값을 반환
abs(): 절댓값을 반환
pow(): 거듭 제곱을 반환
round(): 반올림한 값을 반환
'''

# random 모듈: 난수를 발생시키는 모듈이다.
'''
random(): 0이상 1미만의 난수 발생
randint(n1, n2): n1이상 n2이하의 난수 발생
randrange(n1, n2): n1이상 n2미만의 난수 발생
sample(range(n1, n2), n3): n1이상 n2미만의 난수 n3개 발생(중복 없이)
choice(): 무작위로 1개 아이템 선택함
shuffle(): 아이템 순서 섞음
'''

import random

print(f'random(): {random.random()}') # 0이상 1미만 난수
print(f'randint(): {random.randint(0, 9)}') # 0이상 9이하 난수
print(f'randrange(): {random.randrange(0, 9)}') # 0이상 9미만 난수
print(f'sample(): {random.sample(range(0, 10),3)}') # 0이상 10미만 3개 난수

listVar =  [1, 2, 3, 4, 5, 6]
# 무작위로 1개 아이템 선택
print(f'choice: {random.choice(listVar)}')
print(f'choice: {random.choice(listVar)}')

# 아이템 순서 섞음
random.shuffle(listVar)
print(f'listVar: {listVar}')
random.shuffle(listVar)
print(f'listVar: {listVar}')

# time 모듈: 시간 관련 모듈(UTC)
'''
localtime(): 시스템의 현재 시간을 반환
gmtime(): GMT 시간을 반환
strftime(): 시간 포맷 코드에 따른 출력
'''

import time

lt = time.localtime()        # 시스템 시간
print(f'lt: {lt}')

print(f'년도: {lt.tm_year}')    # 년도 2026
print(f'월: {lt.tm_mon}')       # 월 5

week = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

print(f'요일: {week[lt.tm_wday]}')    # 요일 (화요일)
'''
0: 월요일
1: 화요일
2: 수요일
3: 목요일
4: 금요일
5: 토요일
6: 일요일
'''

gt = time.gmtime()      # GMT 시간
print(f'gt: {gt}')

print(f'gt.tm_hour: {gt.tm_hour}')  # 시간

print(f'시:분:초: {time.strftime('%H:%M:%S', time.localtime())}')
print(f'년:월:일 시:분:초: --> {time.strftime('%Y:%m:%d %H:%M:%S', time.localtime())}')

 