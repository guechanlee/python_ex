
import os
import json
import session
import config as root_config
from memo import config as memo_config


class MemoService:
    def __init__(self):
        self.memos = {}
        self.init_database()


    def init_database(self):    
       # 현재 파일 위치
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        # 프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')

        # db/memos.json
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'memos.json')
        print(f'self.dbFile: {self.dbFile}')
        # C:\lgc\python\python_ex\myDashboradPjt\db\memos.json

        # 파일 존재 여부 확인
        if not os.path.exists(self.dbFile):
            self.save_memos(self.memos)
        else:
            self.memos = self.load_memos()


    # 애플리케이션의 데이터를 JSON 파일 저장 하는 것
    def save_memos(self, memos):    # {}
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(memos, f, ensure_ascii=False, indent=4)

    # JSON 파일을 읽어서 애플리케이션으로 데이터를 가져오는 것
    def load_memos(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)
        
    def isMyMemos(self):
        allMemos = self.load_memos()
        if session.getSignInedMemberId() in allMemos:
            return True
        
        return False


    def run(self):

        if session.getSignInedMemberId() == '': # 로그인 되어있는지 확인
            print('Please SIGN-IN!!')
            return    
        
        flag = True
        while flag:
            # 내방에 메모가 없다면?
            if not self.isMyMemos():
                # 방을 만들어라 [리스트로]
                self.memos[session.getSignInedMemberId()] = []
                # 파일을 저장
                self.save_memos(self.memos)

            menuNum = int(input('1.WRITE    2.READ     3.UPDATE     4.DELETE     99.SERVICE-OUT '))
            if menuNum == memo_config.WRITE:
                newMemo = input('Write new memo: ')
                
                # 로그인 되어있는 정보를 가져온다
                self.memos = self.load_memos()
                myMemos = self.memos[session.getSignInedMemberId()]
                myMemos.insert(0, newMemo)

                # 저장한다
                self.save_memos(self.memos)
                print('WRITE SUCCESS!!')
                
                # 정말 json파일이 잘 들어왔는지 출력
                if root_config.DEV_MOD:
                    print(f'self.load_memos(): {self.load_memos()}')

            elif menuNum == memo_config.READ:
                # 딕셔너리 타입 정보를 가져온다
                self.memos = self.load_memos()
                # 내 것만 뽑는다
                myMemos = self.memos[session.getSignInedMemberId()]
                # 숫자와 메모를 같이 출력한다
                for idx, memo in enumerate(myMemos):
                   print(f'[{idx + 1}] {memo}')

            elif menuNum == memo_config.UPDATE:
                # 딕셔너리 타입 정보를 가져온다
                self.memos = self.load_memos()
                # 내 것만 뽑는다
                myMemos = self.memos[session.getSignInedMemberId()]
                # 숫자와 메모를 같이 출력한다
                for idx, memo in enumerate(myMemos):
                   print(f'[{idx + 1}] {memo}')

                selectedNumber = int(input('Please select the nember to modify: '))
                memo = input('Edit memo: ')
                # 1을 올려준거 다시 내려준다
                myMemos[selectedNumber-1] = memo

                # Json파일에 저장
                self.save_memos(self.memos)
                print('MODIFY SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_memos(): {self.load_memos()}')


            elif menuNum == memo_config.DELETE:
                # 딕셔너리 타입 정보를 가져온다
                self.memos = self.load_memos()
                # 내 것만 뽑는다
                myMemos = self.memos[session.getSignInedMemberId()]
                # 숫자와 메모를 같이 출력한다
                for idx, memo in enumerate(myMemos):
                   print(f'[{idx + 1}] {memo}')

                # 삭제할 정보 입력받기
                selectedNumber = int(input('Please select the nember to delete: '))
                # 삭제 1올려놨던거 다시 내리기
                myMemos.pop(selectedNumber-1)
                self.save_memos(self.memos)

                if root_config.DEV_MOD:
                    print(f'self.load_memos(): {self.load_memos()}')


            elif menuNum == memo_config.SERVICE_OUT:
                flag = False

if __name__ == '__main__':
    memoService = MemoService()
    memoService.run()
