from config_dir.dir import config
from member import session
from db import member_db
from member import member_dumy

if config.DEV_MOD:
    member_dumy.memberDumyInit()
    print(f'memberDB: {member_db.memberDB}')

flag = True

while flag:

    menuNum = ''
    if session.signInedMemberId == '':
        # sign out 상태
        menuNum = int(input('1.sign-up    2.sign-in    99.end'))
    else:
        # sign in 상태
        menuNum = int(input('3.modify    5.sign-out    4.delete    99.end'))

    if menuNum == config.SIGN_UP:
        print('1.sign-up')
        uId = input('Please input new member ID: ')
        uPw = input('Please input new member PW: ')
        uMail = input('Please input new member MAIL: ')
        uPhone = input('Please input new member PHONE: ')

        member_db.memberDB[uId] = {
            'uId': uId,
            'uPw': uPw,
            'uMail': uMail,
            'uPhone': uPhone
        }

        print('New member sign-up success!!')

        if config.DEV_MOD:
            print(f'memberDB: {member_db.memberDB}')

    elif menuNum == config.SIGN_IN:
        print('2.sign-in')
        uId = input('Please input member ID: ')
        uPw = input('Please input member PW: ')

        if uId in member_db.memberDB:
            if member_db.memberDB[uId]['uPw'] == uPw:
                print('sign-in success!!')
            else:
                print('sign-in fail!! -- PW error')
        else:
            print('sign-in fail!! -- ID error')

    elif menuNum == config.MEMBER_MODIFY:
        print('3.modify')
    elif menuNum == config.MEMBER_DELETE:
        print('4.delete')
    elif menuNum == config.SYSTEM_OUT:
        print('99.end')
        flag = False
    elif menuNum == config.SIGN_OUT:
        print('5.sign_out')
