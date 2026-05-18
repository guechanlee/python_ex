
# flag = True

# members = {}    # 데이터 베이스

# while flag:
#     selectedMenuNum = int(input('1. 회원가입 2. 프로그램 종료'))
    
#     if selectedMenuNum == 1:
#         id = input('아이디: ')
#         pw = input('비밀번호: ')
#         members[id] = pw

#     elif selectedMenuNum == 2:
#         flag = False
        
#     for key in members.keys():
#         print(f'ID: {key}, PW: {members[key]}')


# classes =  {'python':'5학점', 'C/C++':'5학점', 'HTML5':'3학점', 'Java':'5학점', 'Javascript':'3학점'}

# classes['HTML5'] = '5학점'
# classes['avascript'] = '5학점'
# print(f'{classes['HTML5']}')
# print(f'{classes['avascript']}')

# 아니면 

# for key in classes:
#     if classes[key] == '3학점':
#         classes[key] = '5학점'
# print(classes)

'''
members = {
    '2019-052001': ['박찬호', 25, 'M', '010-1234-5678', '헬스, 수영', 0],
    '2019-052004': ['박용택', 65, 'M', '010-9012-3456', '수영', 50],
    '2019-052003': ['박세리', 70, 'W', '010-7890-1234', '아쿠아로빅', 50]
}

# 전체 회원 정보 출력
for key in members:
    print(f'회원정보:{key}, 회원정보: {members[key]}')

# 전체 회원 정보 출력을 하는데, 이때 회원의 이름과 성별만 출력을 하자!
for key, value in members.items():
    print(f'회원정보:{key}, 회원정보(이름, 성별): {value[0]}, {value[2]}')
'''

# 리펙토링

# members = {
#     '2019-052001': {
#         '이름': '박찬호',
#         '나이': 25,
#         '성별': 'M',
#         '연락처': '010-1234-5678',
#         '이용서비스': ['헬스', '수영'],
#         '할인율': 0
#     },
#     '2019-052004': {
#         '이름': '박용택',
#         '나이': 65,
#         '성별': 'M',
#         '연락처': '010-9012-3456',
#         '이용서비스': ['수영'],
#         '할인율': 50
#     },
#       '2019-052003': {
#         '이름': '박세리',
#         '나이': 70,
#         '성별': 'W',
#         '연락처': '010-7890-1234',
#         '이용서비스': ['아쿠아로빅'],
#         '할인율': 50
#     }
# }


# # 전체 회원 정보 출력
# for key in members:
#     print(f'회원정보:{key}, 회원정보: {members[key]}')

# print('-' * 30)

# # 전체 회원 정보 출력을 하는데, 이때 회원의 '이름'과 '성별'만 출력을 하자!
# for key, value in members.items():
#     print(f'회원번호: {key}, 회원정보(이름, 성별): {value['이름']}, {value['성별']}')

# print('-' * 30)

# # 전체 회원 정보 출력을 하는데, 어때 회원의 '이름'과 '성별' 그리고 '이용서비스' 만 출력을 하자!
# for key, value in members.items():
#     print(f'회원번호: {key}, 회원정보(이름, 성별): {value['이름']}, {value['성별']}, {value['이용서비스']}')

# # 전체 회원 정보 출력을 하는데, 어때 회원의 '이름'과 '성별', '이용서비스' 그리고 이용서비스개수 만 출력을 하자!
# for key, value in members.items():
#     print(f'회원번호: {key}, 회원정보(이름, 성별): {value['이름']}, {value['성별']}, {value['이용서비스']}, {len(value['이용서비스'])}')



# 야채 개수 입출고
# vegeTables = {
#     '당근': 10,
#     '건대추': 100,
#     '대파': 20,
#     '애호박': 3,
#     '부추': 1
# }

# # 소비
# vegeTables['당근'] -= 1
# vegeTables['건대추'] -= 10
# vegeTables['대파'] -= 1
# vegeTables['애호박'] -= 1
# vegeTables['부추'] -= 1

# for key, value in vegeTables.items():
#     print(f'현재 {key} 재고는: {value}')

# memberInfo = {
#     'id': 'apple123',
#     'pw': '1111'
# }


# for key,velue in memberInfo.items():
#     print(f'{key} {velue}')










# # 용돈기입장

# money = {}
# inMoney = 0


# while True:
#     day = int(input('용돈 기입 날짜를 입력: '))

#     times = input('시간정보 입력: ')       
#     why = input('이유 입력: ')        
#     who = input('누구에게 받았는지 입력: ')       
    
#     init = int(input('입금할 금액: '))
#     inMoney += init

#     outit = int(input('지출한 금액: '))        
#     inMoney -= outit
    

#     money[day] = {
#         '시간': times,
#         '이유': why,
#         '받은사람': who,
#         '입금': init,
#         '지출': outit,
#         '잔액': inMoney
#     }

#     print(f'현재 잔액: {inMoney}원')


#     print(f'\n날짜: {day}')
#     print(f"시간: {money[day]['시간']}")
#     print(f"이유: {money[day]['이유']}")
#     print(f"받은사람: {money[day]['받은사람']}")
#     print(f"입금: {money[day]['입금']}원")
#     print(f"지출: {money[day]['지출']}원")
#     print(f"잔액: {money[day]['잔액']}원")








members = {
    
    '260421' : {
        '이름': '이규찬',
        '나이': '27',
        '번호': '010-2845-2185',
        '키': '184',
        '몸무게': '84'
    },    
    '260422' : {
        '이름': '이서린',
        '나이': '22',
        '번호': '010-2834-2185',
        '키': '172',
        '몸무게': '75'
    },
    '260423' : {
        '이름': '신재연',
        '나이': '50',
        '번호': '010-2846-2185',
        '키': '168',
        '몸무게': '70'
    },
    '260429' : {
        '이름': '이창준',
        '나이': '60',
        '번호': '010-2848-2185',
        '키': '178',
        '몸무게': '80'
    }
}

for key in members:
    print(f'{key} {members[key]}')

    print(f'{members[key]}')

for key, value in members.items():
    print(f'{key} {value['이름']} {value['나이']}')


:: 용돈 기입장 :::::
from datetime import datetime

MENU_INCOME     = 1
MENU_EXPENSE    = 2
MENU_VIEW       = 3
EXIT            = 99

flag = True
DEV_MOD = True

bankAccount = []
currentMoney = 0

if DEV_MOD:
    txt =  '[2026-05-15 15:14:08] \t 100 \t\t aaaaa \t\t 100'
    bankAccount.append(txt)
    txt = '[2026-05-15 15:15:08] \t 200 \t\t bbbbb \t\t 300'
    bankAccount.append(txt)
    txt = '[2026-05-15 15:16:08] \t\t -50 \t ccccc \t\t 250'
    bankAccount.append(txt)

while flag:

    selectedMenuNum = int(input('1.수입    2.지출    3.조회    99.시스템종료 -----> '))
    if selectedMenuNum == MENU_INCOME:
        incomeMoney = int(input('수입 금액: '))
        incomeDesc = input('수입 내용: ')
        currentMoney += incomeMoney

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        txt = f'[{now}] \t {incomeMoney} \t {incomeDesc} \t\t\t {currentMoney}'
        bankAccount.append(txt)

    elif selectedMenuNum == MENU_EXPENSE:
        expenseMoney = int(input('지출 금액: '))
        expenseDesc = input('지출 내용: ')
        currentMoney -= expenseMoney

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        txt = f'[{now}] \t\t\t -{expenseMoney} \t {expenseDesc} \t {currentMoney}'
        bankAccount.append(txt)

    elif selectedMenuNum == MENU_VIEW:
        print('-' * 63)
        print('날짜&시간 \t\t 입금 \t 출금 \t 내역 \t\t 잔액')
        print('-' * 63)
        for item in bankAccount:
            print(item)
        print('-' * 63)

    elif selectedMenuNum == EXIT:
        flag = False 


