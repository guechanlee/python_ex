import lotto_ex  as lm

nums = []

print('1부터 45까지의 정수 6개를 입력 ')
nums.append(int(input('1 번째 숫자를 입력: ')))
nums.append(int(input('2 번째 숫자를 입력: ')))
nums.append(int(input('3 번째 숫자를 입력: ')))
nums.append(int(input('4 번째 숫자를 입력: ')))
nums.append(int(input('5 번째 숫자를 입력: ')))
nums.append(int(input('6 번째 숫자를 입력: ')))

lm.setUNumbers(nums)        # 사용자가 선택한 번호들
lm.setRNumbers()            # 컴퓨터가 선택한 번호들

print(f'이번 주 로또 번호: {lm.getRNumbers()}')
print(f'내가 선택한 로또 번호: {lm.getUNumbers()}')
print(f'일치하는 번호: {lm.compareNumbers()}')