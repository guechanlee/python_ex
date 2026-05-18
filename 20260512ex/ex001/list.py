# 리스트(list)
# fruits = ['사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나']
# print(f'fruits: {fruits}')
# print(f'type of fruits: {type(fruits)}')

# # 리스트와 데이터
# '''
# 리스트에 포함되는 데이터는 어떤 자료형이든 상관없습니다.
# 예를 들어 정수, 실수, 문자(열)이 하나의 리스트로 묶일 수도 있습니다.
# '''

# complexList = [10, 3.14, 'a', 'hello']
# # 이렇게 하나의 리스트에 다양한 데이터 타입의 데이터를 넣을 수 있는 언어는
# # 파이썬과 javascript뿐이다. java는 안된다.


# print(f'complexList: {complexList}')
# print(f'type of complexList: {type(complexList)}')

# member = []
# print(f'member: {member}')
# print(f'type of member: {type(member)}')



# 다음 회의 참석자 명단을 리스트로 선언하고 attendList 변수에 담아보자.
# attendList = ['이순철', '이병헌', '김민우', '박찬호', '김민태']

# how to 리스트의 아이템 조회
# 특정 아이템 조회

#           0       1      2      3      4     5       6         7
# fruits = ['사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나']
# print(f'fuilts: {fruits[1]}')
# print(f'fuilts: {fruits[8]}')
# # 만약 리스트에서 존재하지 않는 인덱스를 참조하면 어떻게 될까요?
# # print(f'fruits[8]: {fruits[8]}')
# # 당연히 에러가 발생합니다. 다음 코드로 확인해봅시다.(IndexError: list index out of range)

# 리스트 길이(아이템 개수) 조회
'''
리스트 길이란 리스트의 아이템 개수를 뜻하는 것으로 len() 함수를 사용하면 알 수 있습니다.
다음은 len() 함수를 이용해서 리스트의 길이를 확인하는 코드입니다.
'''
# numbers = [1, 2, 3, 4, 5]

# print(f'numbers: {numbers}')
# print(f'numbers length: {len(numbers)}')

# # 첫 번째 데이터 조회:
# numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 99]
# print(f'첫 번째 데이터: {numbers[0]}')

# # 마지막 데이터 조회: 0부터 시작함으로 -1
# print(f'마지막 데이터: {len(numbers)-1}')

# # len() 함수는 문자열의 길이를 조회하는데에도 사용된다.
# str = 'helllllllllllllllllllllllo'
# print(len(str))

# quiz) 입력한 글자 수 확인하기
'''
사용자로부터 메세지를 입력 받고, 입력 받은 문자열의 길이를 출력하는 프로그램을 만들어봅시다
'''
# msg = input('메세지 입력: ')
# msgLen = len(msg)
# print(f'msgLen: {msgLen}')


# 리스트 전체 데이터 조회
# balls = ['야구공' , '축구공', '탁구공', '골프공', '농구공']
# print(f'{balls[0]}')
# print(f'{balls[1]}')
# print(f'{balls[2]}')
# print(f'{balls[3]}')
# print(f'{balls[4]}')

# for 문 사용해보기

# idx = 0
# for item in (balls):
#     print(f'item: {item}, index: {idx}')
#     idx += 1



# for idx, item in enumerate(balls):
#     print(f'item: {item}, index: {idx}')

# for num1, num2 in enumerate(balls):
#     print(f'item: {num2} index: {num1}')

# while로 사용해보기    
# balls = ['야구공' , '축구공', '탁구공', '골프공', '농구공']


# i = 0
# while i < len(balls):
#     print(f'item: {balls[i]},index: {i}')
#     i += 1


    
# numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 99]

# #첫번째 숫자 조회하기
# print(numbers[0])

# #마지막 숫자 조회하기
# print(len(numbers)-1)


# 리스트 전체 데이터 조회
# balls = ['야구공' , '축구공', '탁구공', '골프공', '농구공']

# idex = 0
# for item in (balls):
#     print(f'item: {item}, idex: {idex}')
#     idex += 1


# quiz) 다음 리스트에서 마지막 인덱스 값을 출력하는 프로그램을 만드시오.
# sports = ['baseball', 'basketball', 'tennis', 'golf', 'soccer', 'aaaaa']
# lenVar = len(sports) - 1    # 6 - 1 => 5
# print(sports[lenVar])       # 'aaaaa'

# quiz) 다음 리스트에서 'python' 문자열의 인덱스 값을 출력하는 프로그램을 만드시오.
# languages = ['c/c++', 'c#', 'python', 'java']
# for idx, str in enumerate(languages):
#     if str == 'python':
#         print(f'python idx: {idx}')


# targetIdx = languages.index('python')
# print(targetIdx)

# # 아이템 기존 리스트에 삽입
# # 리스트 마지막에 삽입
# sports = ['football', 'baseball', 'volleybal']
# print(f'sports: {sports}')      #['football', 'baseball', 'volleyball']

# sports.append('basketball')
# print(f'sports: {sports}')      #['football', 'baseball', 'volleyball', 'basketball']
# print(f'sports lenght: {len(sports)}')

# quiz) 취미 추가하기
'''
취미들을 저장할 리스트를 정의하고 사용자가 입력한 취미를 추가 되는 프로그램을 만들어보자
그리고 취미의 개수를 출력하자
'''

# hobbies = []

# while True:
#     hobby = input('취미 입력: ')
#     hobbies.append(hobby)   
#     print(f'hobbies: {hobbies}')
#     selectedMenuNumber = int(input('1.취미 추가  2.종료'))
#     if selectedMenuNumber == 2:
#         print(f'총 개수: {len(hobbies)}')
#         break      

# 특정 위치에 아이템 삽입
# 리스트의 원하는 위치에 아이템을 삽입할 때는 insert() 함수를 이용합니다.
# countries = ['korea', 'china', 'japen']  #['korea', 'usa', 'china', 'japen']  
# countries.insert(1, 'usa')
# print(f'countries: {countries}')

# quiz) 누락된 숫자 추가하기
# numbers = [1, 2, 3, 4, 5, 7, 8, 9]     6, 10
# numbers 리스트를 보고 1~10까지 숫자 중 누락된 숫자를 추가해보자.
# numbers = [1, 2, 3, 4, 5, 7, 8, 9]
# numbers.insert(5, 6)
# numbers.append(10)
# print(f'numbers = {numbers}')

# 리스트 연결하기
# 리스트에 또 다른 리스트를 연결할 때는 extend() 함수를 사용합니다.
# list1 = [1, 2, 3]
# print(f'list1: {list1}')
# list2 = [10, 20, 30]
# print(f'list2: {list2}')

# list1.extend(list2)
# print(list1)


# list3 = list1 + list2           # [1, 2, 3, 10, 20, 30]
# print(f'list1: {list1}')
# print(f'list2: {list2}')
# print(f'list3: {list3}')

# list1 = list1 + list2
# print(f'list1: {list1}')
# print(f'list2: {list2}')
# print(f'list3: {list3}')

# 리스트 아이템 삭제하기
# 리스트 마지막 아이템 삭제
# sports = ['football', 'baseball', 'volleyball', 'basketball']
# print(f'sports: {sports}') # ['football', 'baseball', 'volleyball', 'basketball']
# sports.pop(3)
# print(f'sports: {sports}') # ['football', 'baseball', 'volleyball']

# removedItem = sports.pop()            # ['volleyball']
# print(f'removedItem: {removedItem}')  # volleyball

# # pop() 대신 del 키워드를 이용해서 아이템을 삭제할 수 있다.
# sports = ['football', 'baseball', 'volleyball', 'basketball']
# del sports[2]
# print(f'sports: {sports}')

# quiz) sports 리스트에서 'volleyball'을 삭제하는 프로그램을 만들어보자
sports = ['football', 'baseball', 'volleyball', 'basketball']
volleybalidex = sports.index('volleyball')
sports.pop(volleybalidex)
print(f'sports: {sports}')




# favFoods = []

# while True:
# 	food = input('먹고 싶은 음식을 입력하세요')
# 	favFoods.append(food)
# 	print(f'favFoods: {favFoods}')
# 	last = int(input('1.먹을 것 추가  2.종료'))
# 	if last == 2:
# 	    print(f'음식갯수는 : {len(favFoods)}')



