# # 지역변수 vs 전역변수
# # 지역변수는 함수 내부에서 선언된 변수로 함수 내부에서만 사용 가능합니다.
# # 전역변수는 함수 외부에서 선언된 변수로 함수 내/외부에서 사용 가능합니다.

# num = 10

# def fun():
#     # num = 20                # 지역변수
#     global num
#     num = num + 1           # 데이터 수정 num(전역변수) = 10 + 1
#     print(f'num: {num}')    # 10, 전역변수 num > 20 지역변수 num

# print(f'num: {num}')        # 10, 전역변수 num

# fun()

# '''
# global 키워드는 함수 내에서 전역변수의 값을 '수정'하고자 할때 반드시 명시하자!
# '''

# # quiz) 웹사이트의 누적방문 횟수 프로그램
# # 웹사이트 방문 여부를 입력받아 웹사이트의 누적 방문 횟수를 출력해봅시다.

# flag = True
# totalVisitor = 0

# def countVisitor():
#     global totalVisitor
#     totalVisitor += 1

# while flag:
#     selectedMenuNum = int(input('1.웹사이트 방문      2.종료'))

#     if selectedMenuNum == 1 :
#         countVisitor()
#         print(f'누적 방문 횟수: {totalVisitor}')
      
#     else:
#         flag = False
#         print('Good bye~')



# 매개변수(***********************************) 매우중요!
# 매개: 둘 사이에서 양편의 '관계를 맺어' 줌
# 함수를 사용하기 위해 먼저 함수를 정의하고 필요할 때 호출하죠.
# 이 때 함수를 정의하는 쪽을 함수 정의부(선언부), 함수를 호출하는 쪽을 호출부라고 합니다.

# 함수를 호출할 때 데이터를 넘겨줄 수 있는데 이 데이터를 '인수'라고 합니다.
# 함수 정의부는 인수를 받으면 '매개변수'라는 변수에 저장합니다. 그리고 매개변수는 지역변수의 일종입니다.



# # 매개변수 , 지역변수      호출부와 실행부 갯수를 쌍으로 맞춰야한다.
# def greet(name,age):
#     # name = '홍길동' or '박찬호' or '박세리'
#     print(f'{name}님 안녕하세요.나이는 {age}입니다.')

# greet('홍길동', 25)
# greet('박찬호', 20)
# greet('박세리', 30)



# def forecastWeather(temp, humi, rain):
#     print('날씨 예보입니다.')
#     print(f'최고 온도는: {temp}도')
#     print(f'평균 습도: {humi}%')
#     print(f'비올 확율: {rain}%')

# # forecastWeather(35, 70, 80)

# # 인수의 개수를 모르는 경우
# # 우리 학급 학생들의 시험점수 총합과 평균을 구하는 함수를 만들자!
# # 우리 학습 학생수는 총 3명이다.

# # def printScoresForStudents(score1, score2, score3, score4):
# #     totalsScore = score1 + score2 + score3 + score4
# #     averageScore = totalsScore / 4

# #     print(f'총합: {totalsScore}')
# #     print(f'평균: {averageScore}')


# # (*socres) -> 가변인자 -> 변수를 다 더해줌
# def printScoresForStudents(subject, *scores):            # 리스트(list) -> 튜플(tuple)

#     print(f'scores type: {type(scores)}')
#     print(f'scores length: {len(scores)}')

#     totalScore = 0
#     for score in scores:
#         totalScore += score

#     print(f'총합: {totalScore}')
#     averageScore = totalScore / len(scores)
#     # print(f'평균: {totalScore / len(scores)}')

# #     totalsScore = score1 + score2 + score3
# #     averageScore = totalsScore / len(totalsScore)

#     print(f'{subject} 과목 총합: {totalScore}')
#     print(f'{subject} 과목 평균: {averageScore}')

# # # 90
# printScoresForStudents('국어',90, 80, 100, 70)

# # score = int(input('학생 점수 입력: '))
# # printScoresForStudents(score)


# '''
# 선생님이 몇명일지 모르는 학생의 점수를 입력한다.
# 이때 학생 점수의 총합과 평균을 구하는 함수를 만들고 이를 이용하는 프로그램을 만들어보자!
# '''

# flag = True
# studentScores = []

# def printScoresForStudents(scores):     # scores = [,,,,,,,]
#     if len(scores) == 0:
#         print('학생수가 0명이라 총점과 평균을 구할 수 없습니다.')
#     else:
#         totalScore = 0
#         for score in scores:
#             totalScore += score

#         average = totalScore / len(scores)
#         print(f'총점: {totalScore}')           
#         print(f'평점: {average}')   

# while flag:
#     selectedMenuNum = int(input('1.학생 점수 입력     2.종료'))
#     if selectedMenuNum == 1:
#         score = int(input('학생 점수 입력'))
#         studentScores.append(score)

#     else:
#         flag = False

# printScoresForStudents(studentScores)




# quiz) SMS와 MMS 구별하기

# '''
# 문자를 보낼 때 100자 이하인 경우에는 단문 메시지(SMS)로 50원을 부과합니다. 그런데 100자를 
# 넘어가면 장문 메시지(MMS)로 변경되면서 100원이 부과됩니다. 단문과 장문을 구별해서 돈을 부
# 과하는 프로그램을 만들어봅시다. 
# '''


# inputData = input('문자 입력')

# def sendUserMessage(str):
#     strLength = len(str) 
#     print(f'사용자가 입력한 문자 길이: {strLength}')

#     if strLength <= 100:
#         print(f'SMS 발송 완료!')
#         print('50분 부과!')
#     else:
#         print(f'MMS 발송 완료!')
#         print('100분 부과!')
    
# sendUserMessage(inputData)


# 인수와 매개변수의 순서가 일치하지 않을 경우
# def printMemberInfo(name, email, major, grade):                  # 주어 동사 명령어 로 구분할 것
#     print(f'name\t: {name}')
#     print(f'email\t: {email}')
#     print(f'major\t: {major}')
#     print(f'grade\t: {grade}')
#     print('-----------------------------------')

# # printMemberInfo('Hong Gildong', 'gildong@gmail.com', 'art', 1)

# printMemberInfo(email = 'gildong@gmail.com',              # 이렇게 하지말고 꼭 순서 엄격하게 지킬 것
#                 name = 'Hong Gildong',                    # 파이썬만 지원
#                 major = 'art',
#                 grade = 1)

# def printMemberInfo(info):
#     print(f'name: {info['name']}')
#     print(f'name: {info['email']}')
#     print(f'name: {info['major']}')
#     print(f'name: {info['grade']}')

# printMemberInfo({                   # 이름이없는 딕셔너리 어너니머스 딕셔너리
    
#         'name': 'Hong gildong',
#         'email': 'gildong@gmail.com',
#         'major': 'art',
#         'grade' : 1
#     })

# printMemberInfo(memberInfo)

# 매개변수의 기본값 설정
# 직원 급여 지급 프로그램을 만들어보자!
# def setSalary(name,pay = 200):      # 기본 값으로 설정된다 돈이 있으면 넘어가고 없으면 기본값으로 세팅
#     print(f'{name}의 급여 {pay}원 지급!!')

# setSalary('박찬호', 400)
# setSalary('박세리', 600)
# setSalary('박용택')

# [].sort() # reverse = False
# [].sort(reverse = True)      비슷한 느낌이다

# 데이터 반환(return)
# 데이터 반환이란, 함수는 실행이 끝난 후에 결과물(값)을 호출부로 변환할 수 있습니다.
# 이때 사용하는 키워드가 return입니다.
# 덧셈 연산 함수를 만들어 결과를 출력하는 프로그램을 만들어보자!

# def printResult(value):
#     print(f'result: {value}')

# def addFuntion(n1, n2):
#     sum = n1 + n2       # 30
#     # print(f'결과 값: {sum}')
#     printResult(sum)
#     return sum

# addFuntion(10, 20)
# # print(f'result: {result}')

# DEV_MOD = False


# def fun1():         # return은 함수를 종결시킨다.
#     print('222222222222')
#     if DEV_MOD == True:
#           print('111111111111') # 개발단계에서 디버깅 용도로만 사용한다.
#           return
#     print('333333333333')

# fun1()

# 별탑 만들기
def increaseStrat(limitStarCount):
    # print('*')
    # print('**')
    # print('***')
    # print('****')
    # print('*****')
    # print('******')
    # print('*******')
    for n  in range(1, 8):
        print('*'* n)
        if n == limitStarCount:
            break

increaseStrat(5)