# CRUD
'''
C: Create   생성, 추가
R: Read     조회
U: Update   수정
D: Delete   삭제
'''

'''
딕셔너리(Dictionary): {key: value}
'''

# C: Create
student = {
    '학번': 123456789,
    '이름': '홍길동',
    '나이': 20,
    '성별': 'M',
    '연락처': '010-1234-5678'
}

print(f'student: {student}')
print(f'student: {type(student)}')

# R: Read
sNo = student['학번']   # 학번으로 부터 받은 키값 
print(sNo)
print(f'sNo type: {type(sNo)}')

# U: Update
sName = student['이름']
print(f'sName: {sName}')    # 홍길동   >   홍길자

student['이름'] = '홍길자'
sName = student['이름']
print(f'sName: {sName}')    # 홍길자

# D: Delete
del student['연락처']
print(f'student: {student}')

# keys(), values(), items()
# keys(): 딕셔너리 자료형에서 키값들만 몽땅 뽑는다.
# 뽑은 키들은 리스트와 비슷한 데이터 타입이다.
keys = student.keys()
print(f'keys: {type(keys)}')

for key in keys:    #dict_keys(['학번', '이름', '나이', '성별'])
    print(f'keys: value = {key}: {student[key]}')

# values(): 딕셔너리에서 벨류값들만 몽땅 뽑는다
# 뽑은 벨류들은 리스트와 비슷한 데이터 타입이다.
values = student.values()   
print(f'values: {values}')  # dict_values([123456789, '홍길자', 20, 'M'])
print(f'values type: {type(values)}')

for value in values:
    print(f'value: {value}')

items = student.items()     # key & value
print(f'items {items}')     # items dict_items([('학번', 123456789), ('이름', '홍길자'), ('나이', 20), ('성별', 'M')])
for item in items:
    print(f'item: {item}')
    print(f'item[0], item[1]: {item[0]},{item[1]}')

'''
item 튜플 ==> ('학번', 123456789) ==> item[0], item[1]
'''


for key, value in items:        # 구조분해할당 문법
    print(f'key: value = {key}: {value}')

# 구조분해할당
# a, b = (10, 20)
# print(f'a: {a}, b: {b}')

c = (10, 20)
a = c[0]
b = c[1]
print(f'a: {a}, b: {b}')


# a = 10
# b = 20

# # swapping ==> a: 20, b: 10
# temp = a
# a = b       # a: 20
# b = a       # b: 10

# a, b = b, a

scores = [10, 20, 30, 40, 50, 60]
'''
a = 10
b = 20
c = [30, 40, 50, 60]
'''
a, b, *c = scores
print(f'a: {a}')
print(f'b: {b}')
print(f'c: {c}')


# quiz) 다음은 스포츠 센터 회원 정보를 나타낸 표이다.
# 표를 보고 파이썬을 이용해서 컨테이너 자료형으로 만드시오.

members = {
    '2019-052001': {
        '이름': '박찬호',
        '나이': 25,
        '성별': 'M',
        '연락처': '010-1234-5678',
        '이용서비스': ['헬스', '수영'],
        '할인율': 0,
    }
     
     
    #   ['박찬호', 25, 'M', '010-1234-5678', '헬스,수영', 0]
}

# info = members['2019-052001']
# print(f'info {info}')       # '박찬호25M010-1234-5678헬스, 수영+0'
# infos = info.split('+')
# print(f'info: {infos}')     # ['박찬호25M010-1234-5678헬스, 수영', '0']

print(members['2019-052001'])
print(members['2019-052001']['이름'])
print(members['2019-052001']['나이'])
print(members['2019-052001']['할인율'])
print(members['2019-052001']['이용서비스'])

'''
데이터란?
변수
연산자
제어문(조건문, 반복문)
컨테이형 자료구조(list, tuple, dic)
'''


'''
함수(function)'''