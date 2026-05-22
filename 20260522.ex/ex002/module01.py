def fun():
    print('module01의 함수가 실행됩니다.')


print(f'module01의 __name__: {__name__}')

if __name__ == '__main__':
    fun()