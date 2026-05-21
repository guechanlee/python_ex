'''
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다.
메뉴: 1.회원가입    2.로그인    3.특정 회원 정보 출력   4.모든 회원 정보 출력   9.종료
사용자가
'1.회원가입'을 선택하면 회원ID, 회원PW, 회원Email, 회원Phone 정보를 입력받아 회원가입 진행한다.
'2.로그인'을 선택하면 회원ID, 회원PW를 입력받아 로그인 '성공' 또는 '실패'를 출력한다.
'3.특정 회원 정보 출력'을 선택하면 회원ID와 회원PW를 입력받아 일치하는 회원 정보를 모두 출력한다. -> 인증(Authentication) / 인가(Athruization)
'4.모든 회원 정보 출력'을 선택하면 가입되어 있는 모든 회원 정보를 출력한다.
'99.종료'를 선택하면 프로그램 종료 시킨다.

심심하면 > 특정 회원의 회원ID와 회원PW를 입력받아 인증되면 회원 정보를 수정하는 기능을 구현해 보자!!

'''

MEMBER_INFO = {}
flag = True


def registerUser():                 
    userID = (input('회원 ID를 입력하시오'))
    userPW = (input('회원 PW를 입력하시오'))
    userEmail = (input('회원 Email를 입력하시오'))
    userPhoneNum = (input('회원 Phone번호를 입력하시오'))

    MEMBER_INFO['id'] = userID
    MEMBER_INFO['pw'] = userPW
    MEMBER_INFO['email'] = userEmail
    MEMBER_INFO['phone'] = userPhoneNum
    print('회원가입이 완료 되었습니다! 다시 로그인 해주세요!')


def loginUser():
    inputMemberID = (input('회원ID를 입력하세요'))
    inputMemberPW = (input('회원PW를 입력하세요'))
    if inputMemberID == MEMBER_INFO['id']:
        if inputMemberPW == MEMBER_INFO['pw']:
            print('로그인 성공!')
            return True
        else:
            print('비밀번호가 틀렸습니다')
            return False
    else:
        print('아이디가 틀렸습니다')
        return False




while flag:
    userInputData = int(input('1.회원가입   2.로그인    3.특정 회원 정보 출력   4.모든 회원 정보 출력   9.종료'))
    
    if userInputData == 9:
        flag = False
        print('종료')
    
    elif userInputData == 1:
        registerUser()

    elif userInputData == 2:
        loginUser()

    elif userInputData == 3:
       if loginUser() == True: 
            print("=== 회원 정보 ===")
            print(f"ID: {MEMBER_INFO['id']}")
            print(f"Email: {MEMBER_INFO['email']}")
            print(f"Phone: {MEMBER_INFO['phone']}")
            print("=================\n")

    elif userInputData == 4:
        if not MEMBER_INFO:
            print("가입된 회원이 없습니다.\n")
            
        else:
            print(f"모든 회원 정보: {MEMBER_INFO}\n")
    
    else:
        print('번호를 잘못 입력하셨습니다')




MEMBER_INFO = {}    # 값을 입력받아 저장할 상수
flag = True     # 와일문 쓰기 이전 플래그로
FINISH = 9
SIGN_UP = 1
LOGIN = 2
FOUND_MY_INFO = 3
FOUND_EVERY_INFO = 4





def registerUser():  # 첫 함수 (회원가입 할 부품)
    userID = (input('회원 ID를 입력하시오'))
    userPW = (input('회원 PW를 입력하시오'))
    userEmail = (input('회원 Email를 입력하시오'))
    userPhoneNum = (input('회원 phone번호를 입력하시오'))
    MEMBER_INFO[userID] = {
    'PW': userPW,
    'Email': userEmail,
    'PhoneNum': userPhoneNum
}
    print('회원가입이 완료 되었습니다! 다시 로그인 해주세요!')

def loginUser():    # (로그인 할 부품)
    inputMemberID = (input('회원ID를 입력하세요'))
    inputMemberPW = (input('회원PW를 입력하세요'))
 
    if inputMemberID in MEMBER_INFO:        # 중요중요! 멤버인포 딕셔너리에 사용자가 입력한 값이 있는지

        if inputMemberPW == MEMBER_INFO[inputMemberID]['PW']:      # 맴버인포안에 사용자가 입력한 아이디를 조회한 후에 있다면 그 아이디의 비밀번호가 이게 맞는지

            print('로그인 성공!')
            return True
        else:
            print('비밀번호가 틀렸습니다')
            return False
    else:
        print('아이디가 틀렸습니다')
        return False
    
def everyInfo():
      if loginUser() == True:
            print('=== 회원 정보 ===')
            print(f'ID: {MEMBER_INFO['userID']}')
            print(f'Email: {MEMBER_INFO['Email']}')
            print(f'Email: {MEMBER_INFO['PhoneNum']}')
            print('====================\n')



while flag:
    userInputData = int(input('1.회원가입   2.로그인    3.특정 회원 정보 출력   4.모든 정보 출력'))
    # 사용자로부터 입력을 받는다

    if userInputData == FINISH:   # 만약 9번을 선택했다면
        flag = False       
        print('종료')         # 종료

    elif userInputData == SIGN_UP:  # 만약 1번을 선택했다면
        registerUser()       # 미리만들어논 회원가입 함수 가져오기

    elif userInputData == LOGIN:
        loginUser()

    elif userInputData == FOUND_MY_INFO:
        everyInfo()

    elif userInputData == FOUND_EVERY_INFO:
        if not MEMBER_INFO:
            print('가입된 회원이 없습니다.\n')

        else:
            print(f'모든 회원 정보: {MEMBER_INFO}\n')

    else:
        print('번호를 잘못 입력하셨습니다')
    


