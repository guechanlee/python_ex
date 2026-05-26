import config
from util import getDay, getTime


dFlag = True

while dFlag:
    selectedMenuNum = int(input('메뉴: 1.일기작성     2.일기조회      99.종료  --> '))

    if selectedMenuNum == config.DIARY_WRITE:

        print(f'[{getDay()}] 한줄 일기를 작성하세요.')

        todayDiary = input()
        with open('C:/lgc/python/diary.txt','a') as f:
            f.write(f'[{getDay()}{getTime()}] {todayDiary}\n')

    elif selectedMenuNum == config.DIARY_READ:
        
        with open('C:/lgc/python/diary.txt','r') as f:
            str = f.read()
            print(str)

    elif selectedMenuNum == config.SYSTEM_SHUTDOWN:
        print('Bye~')
        dFlag = False