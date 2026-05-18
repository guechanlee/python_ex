# 데이터 중에서 실수는 현존하는 어떤 언어도 완벽하게 다룰 수 없다.
# print(0.1 + 0.2)    # 0.3 > 0.30000000000000004

'''
.1
.2
.3
.4
.5
.6
.7
.8
.9
1

'''
# flt = .1

# while True:
#     print(f'flt: {flt}')    # .1 .2 .3. .4 ~~.9 1.0
#     flt += .1

#     if flt >= 1:
#         break

total = .1 + .2
print(f'total: {total}') #0.30000000000000004
if total > 0.3:
    print('total은 3보다 크다')