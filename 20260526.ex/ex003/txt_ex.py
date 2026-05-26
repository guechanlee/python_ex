# 파일 다루기
'''
[1단계] 파일 열기
파일을 여는 단계 파일을 열기 위해서는 open() 함수를 이용
파일 열기에 성고하면 파일은 객체로 만들어져 메모리에 생성

[2단계] 파일 쓰기/ 읽기
문자열을 쓰거나 읽는 단계 문자열을 쓸 떄는 write() 함수를,
읽을 떄는 read() 함수를 이용

[3단계] 파일 닫기
파일을 닫는 단계 쓰기 또는 읽기가 끝난 파일은 
close()함수를 이용해서 연결을 해체합니다
'''


# open('C:\\lgc\\python\\test.txt', 'w')
# file = open('C:/lgc/python/test.txt', 'w')        # 파일을 '쓰기' 모드로 open한다.
# file.write('Hello python!')                       # 쓰기(write)
# print(f'result: {result}')
# file.close()                                      # 파일 닫기(close, 외부자원 해체)    

# file = open('C:\\lgc\\python\\test.txt', 'r')       # 읽기
# readResult = file.read()
# print(f'readResult: {readResult}')
# print(f'readResult: {type(readResult)}')        # 텍스트 파일은 다 str타입

# readResult = int(readResult)
# readResult += 1
# print(f'readResult: {readResult}')

# file.close()


# file = open('C:/lgc/python/test.txt', 'a')
# file.write('\nhello~')
# file.close()

# with open('C:/lgc/python/test.txt', 'a') as file:
#     for n in range(10):
#         file.write('\nhello~')

# file = open('C:/lgc/python/test.txt', 'a')      # 쓰기모드로 할시 다 날라간다   # a는 파일 끝에 내용 추가
# file.write('\nhi~')
# file.close()


# 예외 처리(보험)
# 세상에 모든 프로그램은 100% 완벽할 수가 없어요.

print(10 + 20)          # 30
try:
    print(10 / 0)       # 에러 발생

except Exception as e:  # e: division by zero
    print(f'e: {e}')
else:
    print('에러가 발생하지 않으면 실행되는 코드')

finally:
    print('에러가 발생하든 않하든 무조건 실행되는 코드')

print(10 - 20)          # X 
print(10 * 20)          # X

# 예외 처리 기본 문법
'''
try ~ except
'''