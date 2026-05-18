# 할당(대입) 연산자
# 할당 연산자는 변수에 값을 대입하는 데 사용하는 연산자로 대입 연산자라고도 합니다.

# # 할당 연산자(=)
# num = 5

# # 복합대입 연산자(+=, -=, *=, /=, %=, //=, **=)
# # num = num + 5
# num += 5

# # num = num * 5
# num *= 5

# #num = num / 5
# num /= 5

# #num = num % 5
# num %= 5

# num = num // 5
# num //= 5

# num = num ** 5
# num **= 5

# quiz) 복리 계산기 만들기
# 회사원인 길동이는 예금 계획을 세우고 있습니다.
# 은행에서 상담을 받아 보니 5년 정기 예금을 복리로 했을 때 
# 가장 큰 목돈을 마련할 수 있다고 알게 되었습니다.
# 길동이가 500만원씩 5년 만기인 정기 예금 상품에 가입했을 때
# 5년 후 받을 총 수령액을 계산해봅시다(이자율: 연 5%)

# myMoney = 5000000
# rate = 0.05

# # 1년 후 총 금액
# myMoney = myMoney + (myMoney * rate)

# # 2년 후 총 금액
# myMoney = myMoney + (myMoney * rate)

# # 3년 후 총 금액
# myMoney = myMoney + (myMoney * rate)

# # 4년 후 총 금액
# myMoney = myMoney + (myMoney * rate)

# # 5년 후 총 금액
# myMoney = myMoney + (myMoney * rate)

# print(f'5년 후 총 수령액:{int(myMoney):,}원')

myMoney = 5000
myMoney *= 1.5
print(myMoney)



