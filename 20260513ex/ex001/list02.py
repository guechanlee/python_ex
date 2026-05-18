# # 리스트 정렬
# '''
# sort() 함수는 리스트의 아이템을 정렬하는 데 사용합니다.
# reverse 옵션이 False면 오름차순(ASC), True면 내림차순(DESC)으로 정렬합니다.
# '''
# numbers = [5, 1, 3, 4, 2, 6]
# print(f'numbers: {numbers}')        # [5, 1, 3, 4, 2, 6]

# # 오름차순(ASC)
# numbers.sort()      # == numbers.sort(reverse=False)
# print(f'numbers: {numbers}')        # [1, 2, 3, 4, 5, 6]

# numbers.sort(reverse=True)
# print(f'numbers: {numbers}')        # [6, 5, 4, 3, 2, 1]

# korean = ['다', '가', '마', '하', '카']
# print(f'korean: {korean}')      # ['다', '가', '마', '하', '카']

# korean.sort()
# print(f'korean: {korean}')      # ['가', '다', '마', '카', '하']

# korean.sort(reverse=True)
# print(f'korean: {korean}')      # ['하', '카', '마', '다', '가']


# scores = [90, 100, 88, 85, 95, 92, 70, 75, 100, 92, 78, 80, 75, 95, 90, 100, 84]

# print(f'scores: {scores}')
# scores.sort()
# print(f'scores: {scores}')
# scores.sort(reverse=True)
# print(f'scores: {scores}')

#  quiz) 회의 참석자 정렬하기
# 다음은 회의 참석자 명단입니다. 참석자 명단을 오름차순과 내림차순으로 정렬해봅시다.
# names = ['홍길동', '김길동', '이길동', '박길동', '정길동']
# names.sort()
# print(f'names {names}')
# names.sort(reverse=True)
# print(f'names {names}')

# # 리스트 순서 뒤집기
# # reverse() 함수를 이용하면 리스트의 아이템을 역순으로 뒤집을 수 있습니다.
# vegetables = ['당근', '오이','양파','감자', '고구마']
# vegetables.reverse
# print(f'vegetables: {vegetables}')   # ['당근', '오이', '양파', '감자', '고구마']



# # 리스트 슬라이싱 (********************)
# # 슬라이싱이란, 리스트에서 필요한 부분의 아이템만 뽑아내는 것을 말합니다.
# animals = ['호랑이', '사자', '곰', '여우', '늑대']
# print(f'animals: {animals}')    #['호랑이', '사자', '곰', '여우', '늑대']

# '''

#           ㅣ----------------ㅣ
# ['호랑이', '사자', '곰', '여우', '늑대']
# '''

# print(f'animals[1:4]: {animals[1:4]}')        #['사자', '곰', '여우']
# print(f'animals: {animals}')                  #['호랑이', '사자', '곰', '여우', '늑대']

# sliceAnimals = animals[1:4]
# print(f'sliceAnimals: {sliceAnimals}')        #['사자', '곰', '여우']

# # [n:m] : n 인덱스부터 (m-1) 인덱스 까지의 아이템을 슬라이싱(추출)한다.

# animals = ['호랑이', '사자', '곰', '여우', '늑대']
# print(f'{animals[:3]}') # ['호랑이', '사자', '곰'] 
# # 인덱스 0부터 2(3-1)까지의 아이템 슬라이싱

# print(f'{animals[3:]}')
# # 인덱스 3부터 끝까지 아이템 슬라이싱


# # 뒤에서 2개의 아이템을 슬라이싱
# print(f'{animals[len(animals)-2:]}')    # ['여우', '늑대']

# print(f'{animals[:-1]}')                # ['호랑이', '사자', '곰', '여우']
# print(f'{animals[1:-1]}')              # ['사자', '곰', '여우']
 
# #                                       # ['호랑이', '사자', '곰', '여우', '늑대']
# print(f'{animals[::2]}')                # ['호랑이', '곰', '늑대']  (한개씩 스탭)

# quiz) 다음 리스트를 보고 답하시오.
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# # alphabet 리스트를 역순으로 출력하시오.
# alphabet.reverse()
# print(f'{alphabet}')

# #2  다음 요구사항에 맞게 alphabet 리스트를 슬라이싱하시오
'''
 - 인덱스 2부터 5까지의 아이템을 출력하시오.
 - 인덱스 0부터 4까지의 아이템을 출력하시오.
 - 인덱스 3부터 7까지의 아이템을 출력하시오.
 - 인덱스 5부터 끝까지의 아이템을 출력하시오.
 - 인덱스 3부터 8까지의 아이템을 출력하시오.
'''
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# # - 인덱스 2부터 5까지의 아이템을 출력하시오.
# print(f'{alphabet[2:6]}')
# # - 인덱스 0부터 4까지의 아이템을 출력하시오.
# print(f'{alphabet[:5]}')
# # - 인덱스 3부터 7까지의 아이템을 출력하시오.
# print(f'{alphabet[3:8]}')
# # - 인덱스 5부터 끝까지의 아이템을 출력하시오.
# print(f'{alphabet[5:]}')
# # - 인덱스 3부터 8까지의 아이템을 출력하시오.
# print(f'{alphabet[3:9]}')

# # 뒤에서 4개 아이템
# print(f'{alphabet[len(alphabet)-4:]}')  #[ 'g', 'h', 'i', 'j']
# print(f'{alphabet[-4:]}')               #[ 'g', 'h', 'i', 'j']


# names = ['홍길동', '김길동', '이길동', '박길동', '정길동']
# print(f'names: {names[-2:]}')
# names.insert(0,'이규찬')
# print(names)

# names = ['홍길동', '김길동', '이길동', '박길동', '정길동']
# name1 = ['이규찬', '이서린']

# names.append(name1)




# # 1.숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기
# num = [3, 7, 1, 9, 5]

# maxNum = 0
# for num in nums:
#         if num > maxNum:        # maxNum:9 num:5 > maxNum = 9
#                maxNum = num      


# # 2. 사용자에게 숫자 입력받아서
# # 1부터 입력한 숫자까지 합계 출력하기 ( 5 )

# userInputData = int(input('숫자를 입력하세요'))
# total = 0
# for num in range(1,userInputData +1):
#         total += num
# print(f'total: {total}')
        


    

# # 3. 리스트에 있는 숫자 중 짝수만 출력하기
# num1 = [1,2,3,4,5,6]
# for n in num1:
#     if n % 2 == 0:
#         print(f'{num1}은 짝수입니다')


# # 4. 리스트 숫자를 오름차순 정렬하기
# num = [5,1,7,3]
# num.sort()
# print(num)
# # 5. 리스트 숫자를 내림차순 정렬하기
# #  [5,1,7,3]
# num = [5,1,7,3]
# num.sort(reverse=True)
# print(num)

# # 6. 리스트 안 숫자의 평균 구하기 [10,20,30]
# num = [10,20,30]
# average = sum(num) + len(num)
# print(f'평균은 {average} 입니다')


# # 7. 리스트에서 가장 작은 숫자 찾기
# #  (min() 사용 금지)
# num1 = [1,2,3,4,5,6]
# minNum = nums[0]
# for num in nums:
#       if num < minNum:
#             minNum = num
# print(f'minNum: {minNum}')  # 1



# # 8. 1부터 100까지 숫자 중
# # 3의 배수와 5의 배수 출력하기
# for i in range(1,101):
      
#     if i % 3 == 0:
#             print(f'{i}는 3의 배수 입니다.')
#     if i % 5 == 0:
#             print(f'{i}는 5의 배수 입니다.')   


# 9. 사용자가 입력한 숫자를 리스트에 저장하다가
# 0 입력하면 종료 후 리스트 출력하기
# [입력: 3 ,입력: 7, 입력: 2 ,입력: 0]

inputList = []

while True:
    inputUserData = int(input('숫자를 입력하세요'))
    
    if inputUserData == 0:
          break

    inputList.append(inputUserData)
     
print(f'최종리스트 {inputList}')


# 마지막 내용: ***********************************************************
# 리스트, 튜플, 딕셔너리

listVar = [3, 3.14, 'hello']
print(f'listVar: {listVar}')

listVar = [3, 3.14, 'hello']
print(f'tupleVar: {tupleVar}')

dictVar = {
     '홍길동': 10,
     '박찬호': '열살',
     '박세리': 3.14,
}
print(f'dictVar: {dictVar}')

