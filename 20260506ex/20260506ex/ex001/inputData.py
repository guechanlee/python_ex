# 데이터 입력(input data)
# input()

'''
print('데이터를 입력하세요.')
inputData = input()
print(inputData)
'''
'''
print('정수를 입력하세요.')
inputInteger = input()
print(inputInteger)
print(type(inputInteger))
'''

'''
print('실수 입력하세요.')
inputFloat = input()       # 3.14
print(inputFloat)          # 3.14
print(type(inputFloat))    # str
'''


# print('논리형 데이터를 입력하세요.',end='')        #end = '' 로 개행을 하지 않는다
# inputBoolean = input()
# print(inputBoolean)
# print(type(inputBoolean))


'''
inputBoolean = input('논리형 데이터를 입력하세요.\n') #논리형 데이터 입력하세요. (자동개행)
print(inputBoolean)                               # True
print(type(inputBoolean))                         # str
'''

#자료형을 변환해야 합니다.
'''
userInputData = input('사용자야~~~~ 정수 입력해라~') # 10
print(userInputData)                             # 10
print(type(userInputData))                       # 10
userInputData = int(userInputData)
print(type(userInputData))
'''

# userInputData = input('True or False 입력하세요.')
# print(userInputData)
# print(type(userInputData))
# bool(userInputData)
# userInputData = bool(userInputData)
# print(type(userInputData))

# #str -> float
# userInputData = input('실수 입력하세요.')
# print(userInputData)
# print(type(userInputData))
# userInputData = float(userInputData)
# print(type(userInputData))


# userInputData = 'true'
# userInputData = bool(userInputData)
# print(type(userInputData))

# x = 3                         #int  3
# y = float(x)                  #int -> float
# print(y)                      # 3.0

# x = 3.141592
# y = int(x)
# print(y)




# name = input('이름을 입력하세요: ')
# age = input('나이를 입력하세요: ')

# print(f'이름: {name}')
# print(f'나이: {age}')

# #두 정수를 입력받아서
#  합, 차, 곱, 평균 출력하는 프로그램 만들어봐

# num1 = int(input('정수를 입력하세요'))
# num2 = int(input('정수를 입력하세요'))
           
# print(f'더하기는 = {num1 + num2} 입니다.')
# print(f'빼기는 = {num1 - num2} 입니다. ')
# print(f'곱은 = {num1 * num2} 입니다. ')
# print(f'평균은 = {(num1 + num2) /2} 입니다. ')






# temp = 0
# num1 = 30
# num2 = 40

# temp = num1
# num1 = num2
# num2 = temp

# print(num1)
# print(num2)





userInputData = bool(input('True or False 입력하세요.:,'))
print(userInputData)
print(type(userInputData))