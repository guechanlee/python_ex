import config
from member import member_service
from bank import bank_service
from memo import memo_service
from todo import todo_service

def main(): # 요청을 받아야한다.
    flag = True
    while flag:
        menuNum = int(input('1.MEMBER     2.BANK      3.MEMO      4.TODO      99.SYSTEM-OUT'))
        if menuNum == config.MEMBER_SERVICE:        # 쉽게 판독하기위해서 상수를 사용
            # memberSerive = member_service.MemberService()
            # memberSerive.run()
            member_service.MemberService().run()

        elif menuNum == config.BANK_SERVICE:
            # bankService = bank_service.BankService()
            # bankService.run()
            bank_service.BankService().run()

        elif menuNum  == config.MEMO_SERVICE:
            memo_service.MemoService().run()

        elif menuNum == config.TODO_SERVICE:
            todo_service.TodoService().run()

        elif menuNum == config.SYSTEM_OUT:
            flag = False

if __name__ == "__main__":
    main()