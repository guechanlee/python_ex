# 모듈
'''
모듈이란 특정 기능을 모아놓은 파일로 모듈을 이용하면 우리가 직접 코딩해야 하는 수고를 덜 수 있습니다.
예를 들어 random 모듈은 난수를 발생시키는 기능을 가지고 있는데, 만약 random 모듈을
사용하지 않고 직접 난수를 발생시키려면 직접 프로그램을 작성해야 하는 수고가 따릅니다.

모듈을 사용하려면 우선 import를 이용해서 모듈을 가지고 와야 합니다.
다음은 random 모듈을 이용해서 주사위 게임에 필요한 난수를 발생시키는 코드입니다.
'''

# import random 
# randomNum = random.randrange(1, 46)
# print(f'randomNum: {randomNum}')

# + = * / ...... > 모듈 > operator 모듈

import operator

print(10 + 20)
print(operator.add(10, 20))