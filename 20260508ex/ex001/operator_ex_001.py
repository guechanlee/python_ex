# quiz
# 수심10 내려갈때 마다 0.7도씩 수온이 감소함
# # 수면(수심)의 온도는 20도
# data = int(input('수심을 입력하세요.'))
# # temperature = 20 - (data // 10 * .7)
# # print(f'temperature: {temperature}')


# # # 속도와 시간을 입력하면 자동차의 주행 거리를 구하는 프로그램을 만들어봅시다.
# # speed = input('주행 속도: ')
# # time = input('주행 시간: ')
# # distance = int(speed) * int(time)
# # print(f'주행 거리: {distance}')

# #quiz
# '''
# A회사는 3대의 컴퓨터로 8시간을 일하면 하루 업무를 처리할 수 있습니다.
# 그런데 단축 근무를 하게 되어 근무 시간이 줄게 되었다면
# 몇 대의 컴퓨터가 더 필요할까요?

# 근무 시간을 입력하면 필요한 컴퓨터 수량을 파악하는 프로그램을 만들어봅시다.
# '''

# # time = int(input('근무 시간을 입력하시오'))
# # computuer = 3 * 8 // time
# # addComputer = 1 if (3 * 8 % time) > 0 else 0

# # totalComputer = computuer + addComputer
# # print(f'필요한 컴퓨터 개수: {totalComputer}')

# # 한 개에 340원 하는 마스크 x개를 구매하고 y원을 지불했을 때
# # 거스름돈 result를 화면에 출력한다.

# maskPice = 340
# maskCount = int(input('마스크 구매 개수'))
# totalPrice = maskPice * maskCount

# cash = int(input('지불 금액:'))

# change = cash - totalPrice 
# print(f'거스름돈: {change}')

# 13시 30분 25초를 초로 나타내는 프로그램을 만드시오.
# print(f'secound: {25 + (60 * 30) + (60 * 60 * 13)}')

# 학생의 국어, 영어, 수학 점수를 입력하면 총점과 평균을 출력하는 프로그램을 만드시오.
# kor = int(input('국어 점수: '))
# eng = int(input('영어 점수: '))
# mat = int(input('수학 점수: '))

# totalScore = kor + eng + mat
# totalAverage = totalScore / 3
# print(f'총점: {totalScore} 평균: {totalAverage}다.')

# print(f'총점은: {kor + eng + mat} 평균은: {(kor+eng+mat)/3}')

# 밤 최저 기온과 낮 최고 기온을 입력하면 일교차를 출력하는 프로그램을 만드시오.

# mT = int(input('밤 최저 기온을 입력하시오'))
# hT = int(input('낮 최고 기온을 입력하시오'))

# total = hT - mT

# print(f'일교차: {total}이다')





# 사용자가 길이(cm)를 입력하면 inch로 환산하는 프로그램을 만드시오(단, 1cm는 0.931inch로 한다).

# cm = float(input('사용자의 길이를 입력하시오'))
# inch = cm * 0.39

# print(f'inch = {inch}')

