import config as root_config
from bank import config as bank_config
import session
import os
import json
import uuid

class BankService:
    def __init__(self):
        self.accounts = {}
        self.init_database()

    def init_database(self):
       # 현재 파일 위치
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        # 프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')

        # db/accounts.json
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'accounts.json')
        print(f'self.dbFile: {self.dbFile}')
        # C:\lgc\python\python_ex\myDashboradPjt\db\accounts.json

        # 파일 존재 여부 확인
        if not os.path.exists(self.dbFile):
            self.save_accounts(self.accounts)
        else:
            self.accounts = self.load_accounts()

            # JSON 파일 저장
    def save_accounts(self, accounts):    # {}
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(accounts, f, ensure_ascii=False, indent=4)

    def load_accounts(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)
        
    # load 끄집어낸다
    # dump 넣는다
        
    def isMyAccount(self):
        allAccounts = self.load_accounts()
        if session.getSignInedMemberId() in allAccounts:
            return True
        
        return False
   
        
    
    def run(self):

        if session.getSignInedMemberId() == '':
            print('Please SIGN-IN!!')
            return

        flag = True
        while flag:

            if self.isMyAccount():
                menuNum = int(input('1.ACCOUNT-LIST   2.NEW-ACCOUNT    3.DEPOSIT      4.WITHDRAWAL    99.SERVICE-OUT '))
            else:
                print('No account yet!!')
                menuNum = int(input('2.NEW-ACCOUNT    99.SERVICE-OUT '))

          

            if menuNum == bank_config.ACCOUNT_LIST:
                pass
            elif menuNum == bank_config.NEW_ACCOUNT:
                self.accounts = self.load_accounts()
                if session.getSignInedMemberId() not in self.accounts:
                    self.accounts[session.getSignInedMemberId()] = {}

                myAccounts = self.accounts[session.getSignInedMemberId()]
                myAccounts[str(uuid.uuid4())] = {
                    'balance': 0,
                    'histories': []
                }

                self.save_accounts(self.accounts)
                print('NEW-ACCOUNT SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'fself.load_accounts: {self.load_accounts}')

            elif menuNum == bank_config.DEPOSIT:
                pass
            elif menuNum == bank_config.WITHDRAWAL:
                pass
            elif menuNum == bank_config.SERVICE_OUT:
                flag = False
          
if __name__ == '__main__':
    bankService = BankService()
    bankService.run()