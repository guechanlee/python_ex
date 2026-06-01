# 함수 or 클래스
# 멤버 서비스에 넣을 기능들을 먼저 기획 후 클래스 만들기
from util import util_time
from member import config as member_config
import config as root_config
import os
import json
import session


class MemberService:
    def __init__(self):
        self.members = {}
        self.init_database()

    # 회원 가입 기능
    def sign_up(self):
        mId = input('Input new member ID: ')
        
        # ID 중복체크를 할 때 self.members를 사용한다.
        if mId in self.members:
            print('이미 사용중인 ID 입니다.')
            return

        mPw = input('Input new member PW: ')
        mMail = input('Input new member MAIL: ')
        mPhone = input('Input new member PHONE: ')


        newMember = {                   # 일종의 기능
            'mId': mId,
            'mPw': mPw,
            'mMail': mMail,
            'mPhone': mPhone,
            'mRegDate': util_time.getCurrentDateTime(), 
            'mModDate': util_time.getCurrentDateTime(),
        }
        
        self.members[mId] = newMember   # 키값을 생성

        # DB(members.json)에 새 회원 정보 저장
        self.save_members(self.members)     # {}

        print('MEMBER SIGN-UP SUCCESS!!')
        
        if root_config.DEV_MOD:
            print(f'self.load_members(): {self.load_members()}')

    # 회원 로그인 기능
    def sign_in(self):
        mId = input('Input member ID: ')
        mPw = input('Input member PW: ')
       
        self.members = self.load_members()
        if mId in self.members and self.members[mId]['mPw'] == mPw:
            print('MEMBER SIGN-IN SUCCESS!!')
            # session.signInedMemberId = mId
            session.setSignInedMemberId(mId)

            if root_config.DEV_MOD:
                print(f'session.signInedMemberId: {session.signInedMemberId}')
            return
        
        print('MEMBER SIGN-IN FAIL!!')
    
    # 회원 로그아웃 기능
    def sign_out(self):
        session.self.setSignInedMemberId('')
        print('SIGN-OUT SUCCESS!!')

    # 회원 정보수정 기능
    def modify(self):
        mPw = input('Input member PW: ')
        mMail = input('Input member MAIL: ')
        mPhone = input('Input member PHONE: ')

        self.members = self.load_members()
        memberForModify = self.members[session.getSignInedMemberId()]

        memberForModify['mPw'] = mPw
        memberForModify['mMail'] = mMail
        memberForModify['mPhone'] = mPhone
        memberForModify['mModDate'] = util_time.getCurrentDateTime()

        self.save_members(self.members)

        print(f'MODIFY SUCCESS!!')

        if root_config.DEV_MOD:
            print(f'self.load_members(): {self.load_members()}')


    # 회원 탈퇴 기능
    def delete(self):
        confirm = input('정말 탈퇴하시겠습니까? [Y] or [N]')
        if confirm == 'Y':
            self.members = self.load_members()
            del self.members[session.getSignInedMemberId()]
            self.save_members(self.members)
            session.setSignInedMemberId()
            print('DELETE SUCCESS!!')

        if root_config.DEV_MOD:
            print(f'self.load_members(): {self.load_members()}')
    

    def run(self):
        flag = True
        while flag:
            if session.signInedMemberId ==  '':
                 menuNum = int(input('1.SIGN-IP    2.SIGN-IN      99.SERVICE-OUT '))
            else:
                 menuNum = int(input('3.SIGN-OUT      4.MODIFY        5.DELETE        99.SERVICE-OUT '))
           
           
            
            if menuNum == member_config.SIGN_IP:
                self.sign_up()
            elif menuNum == member_config.SIGN_IN:
                self.sign_in()
            elif menuNum == member_config.SIGN_OUT:
                self.sign_out()
            elif menuNum == member_config.MODIFY:
                self.modify()
            elif menuNum == member_config.DELETE:
                self.delete()
            elif menuNum == member_config.SERVICE_OUT:
                flag = False

    def init_database(self):
        
        # 현재 파일 위치
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        # 프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')

        # db/members.json
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'members.json')
        print(f'self.dbFile: {self.dbFile}')
        # C:\lgc\python\python_ex\myDashboradPjt\member

        # 파일 존재 여부 확인
        if not os.path.exists(self.dbFile):
            self.save_members(self.members)
        else:
            self.members = self.load_members()

    # JSON 파일 저장
    def save_members(self, members):    # {}
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(members, f, ensure_ascii=False, indent=4)

    def load_members(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)

    # load 끄집어낸다
    # dump 넣는다

if __name__ == '__main__':          # 메인파일을 잠시 가져옴 (테스트 용)
    memberService = MemberService()     # memberService라는 함수를 변수에 다가 넣어준 후
    memberService.run()             # memberService에 있는 많은 함수들 중에 sign_up 함수만 작동시켜줘  -> run 함수만 작동 