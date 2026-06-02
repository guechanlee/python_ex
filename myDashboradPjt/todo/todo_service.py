'''자료구조
todos -> dic
{
gildong = [
    {
        tText: '청소',
        tExpDate: '2026-07-01 11:00:00',
        tComplete: True,
        tRegDate: 2026-06-02 10:00:00,
        tModDate: 2026-06-02 10:00:00
    },
    {
        tText: '청소',
        tExpDate: '2026-07-01 11:00:00',
        tComplete: True,
        tRegDate: 2026-06-02 10:00:00,
        tModDate: 2026-06-02 10:00:00
    }
    ]
}

'''

import os
import json
import session
import config as root_config
from todo import config as todo_config
from util import util_time


class TodoService:
    def __init__(self):
        self.todos = {}
        self.init_database()

    def init_database(self):
       # 현재 파일 위치
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        # 프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')

        # db/accounts.json                  db파일에  이런이름에 json파일을 만든다
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'todos.json')
        print(f'self.dbFile: {self.dbFile}')
        # C:\lgc\python\python_ex\myDashboradPjt\db\todos.json

        # 파일 존재 여부 확인
        if not os.path.exists(self.dbFile):
            self.save_todos(self.todos)
        else:
            self.todos = self.load_todos()

            # JSON 파일 저장
    def save_todos(self, todos):    # {}
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(todos, f, ensure_ascii=False, indent=4)

    def load_todos(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)
        
    # load 끄집어낸다
    # dump 넣는다
        
    def isMytodos(self): # 나의 방이 있냐 없냐
        allTodos = self.load_todos()
        if session.getSignInedMemberId() in allTodos:
            return True
        
        return False

    def run(self):
        # 로그인 되어있는지 확인
        if session.getSignInedMemberId() == '':
            print('Please Sign-in')
            return

        flag = True
        while flag:
            # 나의 방이 없다면? 방을 만들고
            if not self.isMytodos():
                self.todos[session.getSignInedMemberId()] = []
                self.save_todos(self.todos)

            menuNum = int(input('1.WRITE   2.READ   3.UPDATE   4.DELETE   5.COMPLETE-CHANGE   99.SERVICE-OUT '))
            if menuNum == todo_config.WRITE:
                # 로드 파일로 정보 가져오기
                self.todos = self.load_todos()
                # 내 파일만 가져오기
                myTodos = self.todos[session.getSignInedMemberId()]

                # 텍스트를 입력 받기
                tText = input('Input new todo txt: ')
                tExpDate = input('Input todo experation date(2026-08-05 06:09:09)')
                
                # 자료 구조 넣기
                todo = {
                    'tTxt': tText,
                    'tExpDate': tExpDate,
                    'tRegDate': util_time.getCurrentDateTime(),
                    'tModDate': util_time.getCurrentDateTime(),
                    'tComplete': False
                }
                
                myTodos.insert(0, todo)
                self.save_todos(self.todos)
                print('WRITE SUCCESS!!')

                # 육안으로 보기
                if root_config.DEV_MOD:
                    print(f'self.load_todos(): {self.load_todos()}')


            elif menuNum == todo_config.READ:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getSignInedMemberId()]
                for idx, myTodo in enumerate(myTodos):
                    print('-' * 50)
                    print(f'[{idx + 1}]')
                    print(f'TEXT: {myTodo["tTxt"]}')
                    print(f'EXPIARATIONDATE: {myTodo["tExpDate"]}')
                    print(f'REGISTE DATE: {myTodo["tRegDate"]}')
                    print(f'MODIFY DATE: {myTodo["tModDate"]}')
                    print(f'COMPLETE: {myTodo["tComplete"]}')
                    print('-' * 50)


            elif menuNum == todo_config.UPDATE:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getSignInedMemberId()]
                for idx, myTodo in enumerate(myTodos):
                    print('-' * 100)
                    print(f"[{idx+1}] {myTodo['tTxt']} [{myTodo['tExpDate']}] [{myTodo['tComplete']}]")
                    print('-' * 100)

                todoNumber = int(input('Enter the todo number: '))
                tText = input('Input new todo txt: ')
                tExpDate = input('Input todo experation date(2026-08-05 06:09:09')

                todo = {
                    'tTxt': tText,
                    'tExpDate': tExpDate,
                    'tRegDate': myTodos[todoNumber-1]['tRegDate'],
                    'tModDate': util_time.getCurrentDateTime(),
                    'tComplete': myTodos[todoNumber-1]['tComplete']
                }

                myTodos[todoNumber-1] = todo
                self.save_todos(self.todos)
                print('UPDATE SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_todos(): {self.load_todos()}')

            elif menuNum == todo_config.DELETE:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getSignInedMemberId()]
                for idx, myTodo in enumerate(myTodos):
                    print('-' * 100)
                    print(f"[{idx+1}] {myTodo['tTxt']} [{myTodo['tExpDate']}] [{myTodo['tComplete']}]")
                    print('-' * 100)

                todoNumber = int(input('Enter the todo number: '))
                myTodos.pop(todoNumber-1)
                self.save_todos(self.todos)
                print('DELETE SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_todos(): {self.load_todos()}')

            
            elif menuNum == todo_config.COMPLETE_CHANGE:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getSignInedMemberId()]
                for idx, myTodo in enumerate(myTodos):
                    print('-' * 100)
                    print(f"[{idx+1}] {myTodo['tTxt']} [{myTodo['tExpDate']}] [{myTodo['tComplete']}]")
                    print('-' * 100)

                todoNumber = int(input('Enter the todo number: '))
                # if myTodos[todoNumber-1]['tComplete'] == True:
                #     myTodos[todoNumber-1]['tComplete'] == False
                # else:
                #     myTodos[todoNumber-1]['tComplete'] == True
                
                myTodos[todoNumber-1]['tComplete'] = not myTodos[todoNumber-1]['tComplete']
                self.save_todos(self.todos)
                print('COMPLETE CHANGE SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_todos(): {self.load_todos()}')    

            elif menuNum == todo_config.SERVICE_OUT:
                flag = False            






if __name__ == '__main__':
    todoService = TodoService()
    todoService.run()