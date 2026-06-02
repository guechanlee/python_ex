import config as root_config
from bank import config as bank_config
import session
import os
import json
import uuid
from util import util_time

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
        
    def isMyAccount(self): # 나의 방이 어딨냐
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
            
            # 내 방이 있는가? 로그인 되었을 때
            if self.isMyAccount():
                menuNum = int(input('1.ACCOUNT-LIST   2.NEW-ACCOUNT    3.DEPOSIT      4.WITHDRAWAL    99.SERVICE-OUT '))
            # 로그인 되지 않았을 때
            else:
                print('No account yet!!')
                menuNum = int(input('2.NEW-ACCOUNT    99.SERVICE-OUT '))

          

            if menuNum == bank_config.ACCOUNT_LIST:
                self.accounts = self.load_accounts()
                myAccounts = self.accounts[session.getSignInedMemberId()]

                for idx, myAccount in enumerate(myAccounts.keys()):
                    print('=' * 80)
                    print(f"[{idx + 1}]: {myAccount}: {myAccounts[myAccount]['balance']}")
                    print('-' * 80)
                    print('날짜/시간 \t\t 내역 \t\t\t 입금 \t\t 출금')
                    for history in myAccounts[myAccount]['histories']:
                        if 'dAmount' in history:
                            print(f'{history["dRegDate"]} \t {history["dHistory"]} \t\t\t {history["dAmount"]}')
                        else:
                            print(f'{history["wRegDate"]} \t {history["wHistory"]} \t\t\t\t\t {history["wAmount"]}')
                    print()

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
                self.accounts = self.load_accounts()
                myAccounts = self.accounts[session.getSignInedMemberId()]
                
                print('\nMy Accounts-------------------------------------')
                for idx, account in enumerate(myAccounts.keys()):
                    print(f'[{idx+1}]: {account}')
                print('--------------------------------------------------\n')

                '''
                My Accounts-------------------------------------
                [1]: 326b19c7-81f2-4003-aaeb-fd46bb5f56e7
                [2]: b30be0b8-b674-4b48-9679-1ca7672586af
                --------------------------------------------------
                '''
                depositAccountNumber = ''
                while True:
                    depositAccountNumber = input('Enter deposit account number: ')
                    if depositAccountNumber not in myAccounts:
                        print('The account was not found!!')
                        print('\nMy Accounts-------------------------------------')
                        for idx, account in enumerate(myAccounts.keys()):
                            print(f'[{idx+1}]: {account}')
                        print('--------------------------------------------------\n')   
                    else:
                        break


                depositAmount = int(input('Enter deposit amount: '))
                depositHistory = input('Enter dopdsit history: ')
                deposit = {
                    'dAmount': depositAmount,
                    'dHistory': depositHistory,
                    'dRegDate': util_time.getCurrentDateTime(),
                    'dModDate': util_time.getCurrentDateTime()
                }

                myAccounts[depositAccountNumber]['balance'] += depositAmount
                myAccounts[depositAccountNumber]['histories'].insert(0, deposit)

                self.save_accounts(self.accounts)
                print('DIPOSIT SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_accounts(): {self.load_accounts}')


            elif menuNum == bank_config.WITHDRAWAL:
                self.accounts = self.load_accounts()
                myAccounts = self.accounts[session.getSignInedMemberId()]
                
                print('\nMy Accounts-------------------------------------')
                for idx, account in enumerate(myAccounts.keys()):
                    print(f'[{idx+1}]: {account}')
                print('--------------------------------------------------\n')

                '''
                My Accounts-------------------------------------
                [1]: 326b19c7-81f2-4003-aaeb-fd46bb5f56e7
                [2]: b30be0b8-b674-4b48-9679-1ca7672586af
                --------------------------------------------------
                '''
                withdrawalAccountNumber = ''
                while True:
                    withdrawalAccountNumber = input('Enter withd rawal account number: ')
                    if withdrawalAccountNumber not in myAccounts:
                        print('The account was not found!!')
                        print('\nMy Accounts-------------------------------------')
                        for idx, account in enumerate(myAccounts.keys()):
                            print(f'[{idx+1}]: {account}')
                        print('--------------------------------------------------\n')   
                    else:
                        break


                withdrawalAmount = int(input('Enter withdrawal amount: '))
                withdrawalHistory = input('Enter withdrawal history: ')
                withdrawal = {
                    'dAmount': withdrawalAmount,
                    'dHistory': withdrawalHistory,
                    'dRegDate': util_time.getCurrentDateTime(),
                    'dModDate': util_time.getCurrentDateTime()
                }

                if withdrawalAmount > myAccounts[withdrawalAccountNumber]['balance']:
                    print('Error! Check Balance!!')
                else:
                    myAccounts[withdrawalAccountNumber]['balance'] -= withdrawalAmount
                    myAccounts[withdrawalAccountNumber]['histories'].insert(0, withdrawal)


                
                self.save_accounts(self.accounts)
                print('WITHDRAWAL SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_accounts(): {self.load_accounts}')

            
            
            elif menuNum == bank_config.SERVICE_OUT:
                flag = False
          
if __name__ == '__main__':
    bankService = BankService()
    bankService.run()