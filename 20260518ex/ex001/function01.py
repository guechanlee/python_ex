# # 함수(function) 모듈또는 부품
# # python에서는 함수가 꽃!
# # Java에서는 클래스가 꽃!

# '''
# 프로그래밍의 함수 또한 수학의 함수와 동일하게 값을 넣어주면 특정 기능을
# 수행한 연산 결과를 출력합니다. 여기서 특정 기능이란 덧셈 같은 비교적
# 간단한 연산부터 네트워크 연결, 회원 인증, 메일 발송과 같이 복잡하고 어려운 작업까지 모두 포함합니다.


# 믹서기에 사과를 넣으면 사과 주스가 되고, 오렌지를 넣으면 오렌지 주스가 되듯이
# 사용자는 함수에 값만 집어넣으면 원하는 결과를 얻을 수 있습니다.
# '''

# # 함수의 종류 내장 함수 vs 사용자 함수
# # 코드(기능) 재사용 -> 함수
# # 데이터 재사용 -> 변수

# # 함수 정의하기
# '''
# 사용자 함수를 만든다는 것을 '함수를 정의한다.'라고 합니다.
# 함수를 정의할 때 def 키워드를 사용합니다. 그리고 함수명은 클론(:),
# 실행부를 이용합니다.
# '''

# '''
# def 함수명():
#     실행부(함수 기능)
# '''

# def greet():
#     print('안녕하세요.')
#     print('반갑습니다.')
#     print('저는 홍길동 입니다.')

# '''
# 함수명 규칙
# 1. 내장 함수명과 동일하면 안된다.
# 2. 첫 글자는 주로 소문자로 시작한다.
# 3. 첫 글자로 숫자를 사용할 수 없다. 
# 4. 특수문자는 사용할 수 없지만 언더바(_)는 사용 가능하다.
# 5. 두 개이상의 단어가 조합되는 경우 스네이크 또는 카멜표기법을 사용하자.
# sendMessage():     calculateDistance():
# '''

# # quiz) 온도센서 작동 시스템 만들기
# # 온도센서 작동을 시작하고 멈추는 함수를 정의해봅시다.
# # 함수명은 함수의 기능을 이해하기 좋도록 짓습니다.

# # 함수 선언

# def startTemperatureSensor():
#     print('온도센서 작동을 시작합니다')

# def stopTemperatureSensor():
#     print('온도센서 작동을 중지합니다')


# # 함수 호출
# startTemperatureSensor()
# stopTemperatureSensor()

# # quiz) 내 노트북은 몇 인치일까?
# '''
# 고등학교 졸업 기념으로 노트북을 하나 장만했습니다.
# 노트북 사이즈에 꼭 맞는 파우치를 하나 구매하려고 하는데 사이즈 표에 
# 인치로만 표시되어있습니다.
# cm를 인치로 바꿔주는 함수를 만들어봅시다
# (1inch = 0.393701cm)
# '''

# # def convertUnit():
# #     lengthCM = float(input('길이(cm) 입력: '))
# #     print(f'{lengthCM * 0.393701}inch')

# # convertUnit()
# # convertUnit()
# # convertUnit()

# # quiz) 이동 거리를 계산하는 함수
# '''
# 길동이는 5시간 동안 3km/h의 속도로 등산을 했습니다.
# 길동이가 등산한 시간과 속도를 입력하면 이동한 거리를 계산해주는 프로그램을
# 함수를 이용하여 만들어봅시다
# '''

# def calculateDistance():
#     print(f'이동거리: {hourData * speedData}km ')

# hourData = float(input('이동 시간:'))
# speedData = float(input('속도: '))

# calculateDistance()

# # pass 키워드
# def calculateNumber():
#     pass

# 1



# quiz) 다국어 인사말 프로그램 by 함수
'''
출신 국가를 선택하면 해당하는 국가의 인사말이 출력되는 프로그램을
함수를 이용해서 만들어봅시다.
1.한국      2.USA       3.Japan
'''

# def introKor():
#     print('안녕')

# def introEng():
#     print('Hello')

# def introJap():
#     print('こんにちは')

# selectedMenuNum = int(input('Where are you from? 1.한국      2.USA       3.Japan  '))

# if selectedMenuNum == 1:
#     introKor()

# elif selectedMenuNum == 2:
#     introEng()

# elif selectedMenuNum == 3:
#     introJap()


# quiz) 계산기 프로그램 by 함수
'''
사용자가 숫자 2개를 입력하고 연산자를 선택하면 연산결과가 출력되는 프로그램
을 함수를 이용해서 만들어봅시다.
'''


# 부품을 미리 만들어놓기 (테스트)

# def add():  
#     print(f'덧셈 결과: {inputNumber1 + inputNumber2}')

# def sub():
#     print(f'뺄셈 결과: {inputNumber1 - inputNumber2}')

# def mul():
#     print(f'곱셈 결과: {inputNumber1 * inputNumber2}')

# def div():
#     print(f'나눗셈 결과: {inputNumber1 / inputNumber2}')

# # 이후에 부품을 집어넣기

# def calculator():
#     if selectedOperator == 1:       # 덧셈
#         add()
        
#     elif selectedOperator == 2:     # 뺄셈
#         sub()

#     elif selectedOperator == 3:     # 곱셈
#         mul()

#     elif selectedOperator == 4:     # 나눗셈
#         div()

# inputNumber1 = float(input('숫자를 입력하세요. '))
# selectedOperator = int(input('연산자를 선택하세요. 1.덧셈    2.뺄셈    3.곱셈    4.나눗셈'))
# inputNumber2 = float(input('숫자를 입력하세요. '))


# calculator()

# TDD 실제 코드를 작성하기 전에 테스트 케이스를 먼저 작성하는 소프트웨어 개발 방법론

for num1 in range(2,10):
    for num2 in range(1,10):

        print(f'{num1} x {num2} = {num1 * num2}')