SIGN_UP                 = 1 
SIGN_IN                 = 2
PRINT_MY_INFO           = 3
PRINT_ALL_MEMBER_INFO   = 4
SYSTEM_SHUTDOWN         = 99

DEV_MOD = False

members = {}        # 데이터베이스 Database

if DEV_MOD:                 # 더미데이터

    uIds = ['gildong','chanho', 'saeri']
    uPws = ['1234','5678', '9012']
    uMails = ['gildong@gmail.com', 'chanho@gmail.com', 'saeri@gmail.com']
    uPhones = ['010-1234-5678', '010-1234-1234', '010-9999-1234']

    for n in range(len(uIds)):      # 3회 반복 ( 0, 1, 2 )
        members[uIds[n]] = {
            'uId': uIds[n],
            'uPw': uPws[n],
            'uMails': uMails[n],
            'uPhone': uPhones[n]
        }

# functions START
def getSelectedMenuNum():
    selectedMenuNum = int(input('1.회원가입   2.로그인    3.나의 정보 출력    4.모든 회원 정보 출력   99.종료'))
    return selectedMenuNum

def setNewMember(uId, uPw, uMail, uPhone):
        members[uId] = {
                    'uId': uId,
                    'uPw' : uPw,
                    'uMail' : uMail,
                    'uPhone' : uPhone
                }

def isMember(uid):
    if uId in members:
            print(f'{uId}는(은) 이미 사용중 입니다. 다시 확인하세요.')
            return True
    else:
        return False

def printAllMemberInfo(value):
    for key1, value1 in value.items():
                print(f'{key1}: {value1}')

# functions END


flag = True
while flag:

    userSelectedMenuNum = getSelectedMenuNum()
    if userSelectedMenuNum == SIGN_UP:        # 1.회원가입
        uId = input('Input member ID: ')
        if not isMember(uId):       # False: 회원이 없는 경우(회원가입 진행O)   #True: 회원이 있는 경우(회원가입 진행X)
            uPw = input('Input member PW: ')
            uMail = input('Input member EMAIL: ')
            while True:
                if '@' not in uMail:
                    print('입력한 이메일 주소가 형식에 맞지 않습니다.')
                    uMail = input('Input member EMAIL: ')
                else:
                    break

            uPhone = input('Input member PHONE: ')

            setNewMember(uId, uPw, uMail, uPhone)
      
        print('SIGH-UP SUCCESS!!')

        if DEV_MOD: print(f'members: {members}')


        

    elif userSelectedMenuNum == SIGN_IN:      # 2.로그인 
        signInCount = 1
        while True: 
            uId = input('Input member ID: ')
            uPw = input('Input member PW: ')
            

            if uId in members:
                uInfo = members[uId]
                if uInfo['uPw'] == uPw:
                    print('SIGN-IN-SUCCESS!!')
                else:
                    print('SIGN-IN-FAIL!!')
                    signInCount += 1
                    if signInCount > 3:
                        print('3회 이상 틀렸어요!!')
                        break
            else:
                print('존재 하지 않는 ID입니다. 다시 확인하세요.')

    elif userSelectedMenuNum == PRINT_MY_INFO:      # 3.나의 정보 출력
        if uId in members:
            uInfo = members[uId]
            if uInfo['uPw'] == uPw:
                print('SIGN-IN-SUCCESS!!')

            else:
                print('SIGN-IN-FAIL!!')
        else:
            print('존재 하지 않는 ID입니다. 다시 확인하세요.')

    elif userSelectedMenuNum == PRINT_ALL_MEMBER_INFO:      # 4.모든 회원 정보 출력
        for key, value in members.items():
            print(f'{key}님의 정보 ----------')
            printAllMemberInfo(value)
            print('-' * 30)

    elif userSelectedMenuNum == SYSTEM_SHUTDOWN:     # 99.종료
        flag = False
        print('Good bye~')