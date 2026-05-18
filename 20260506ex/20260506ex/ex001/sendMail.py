# print('회원정보를 입력하세요.')

# userName = input('이름: ')
# userMail = input('메일: ')
# userId = input('아이디: ')
# userPw = input('비밀번호: ')

# print('-----------------------')
# print('To. ' + userMail)
# print('▶ 아이디 및 비밀번호 확인')
# print(userName + ' 고객님의 안녕하세요.')
# print(userName + ' 고객님의 아이디와 비밀번호는 아래와 같습니다.')
# print('아이디:' + userId)
# print('비밀번호:' + userPw)
# print('감사합니다')
# print('Naver 담당자.')
# print('-----------------------')

# userMail = 'gildong@gmail.com'
# print('To')
# print('To. ' + userMail)

# print('2026', '05','06',sep='-')

# print('Hello',end=' ')
# # print('World')

# # f-string (가장 많이 사용)
# name = '철수'
# age = 25

# # 이름은 철수, 나이는 25입니다.
# print('이름은 ' + name + ', 나이는 ' + str(age) + '입니다')
# print(f'이름은 {name}, 나이는 {age}입니다.')
# #print(f'이름은{name}, 나이는 {age}입니다.')

# format() (두 번째로 많이 사용)(********)
# print('이름은 {}, 나이는 {}입니다.'.format(name, age))

# print('이름은 {1}, 나이는 {0}입니다.'.format(age, name))





# k = input('국어점수를 입력하시오') 
# y = input('영어점수를 입력하시오')
# m = input('수학점수를 입력하시오')



# z = input ('정수를 입력')
# s = input ('정수를 입력')
# z = int(z)
# s = int(s)


# print(z + s)

# quiz) var1, var2 변수에는 정수 10과 20이 각각 저장되어 있다.
# var1과 var2의 데이터를 서로 바꾸는 프로그램을 만들고 화면에 var1과 var2의 데이터를 출력하시오.

# var1 = 10
# var2 = 20

# print(f'val1: {var1}, var2: {var2}')

# temp = var1
# var1 = var2
# var2 = temp

# print(f'var1: {var1}, var2: {var2}') 


firstNumber = int(input('점수를 입력하시오'))
secoundNumber = int(input('점수를 입력하시오'))

print(f'합= {firstNumber + secoundNumber}')