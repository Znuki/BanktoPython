# 계좌정보를 이용하여 구현될 기능을 담고 있는 클래스 멤버필드
# 멤버메서드 : makeAccount() - 계좌개설을 담당할 메서드

file = "C:/Users/Sewon/Desktop/likelion/Bank.txt"
all_id = list()  # 모든 id를 담을 리스트 선언

class Account:  # BankManager에서 사용하는 함수를 선언한 클래스
    def __init__(self, userid="", name="", balance=0):
        if (userid == ""):  # 유저 아이디가 없으면 계좌번호, 이름, 예금금액을 입력받는다
            self.userid = input("계좌번호 = ")
            self.name = input("고객이름 = ")
            self.balance = int(input("예금금액 = "))
        else:  # 그 외에는 self.userid에 userid 대입
            self.userid = userid
            self.name = name
            self.balance = balance

    def disp(self):        #showAccount에서 계좌 및 정보를 보여주는 것을 실행하는 함수
        print("계좌번호:{0}\t이름: {1}\t잔액: {2}".format(self.userid, self.name, self.balance))


    def info(self):        #{0}:{1}:{2}자리에 self.userid, self.name, self.balance를 넣는다.
        return "{0}:{1}:{2}\n".format(self.userid, self.name, self.balance)

    def getid(self):       #유저의 계좌를 리턴하는 함수
        return self.userid

    def deposit(self, money):       #금액을 예금하는 함수
        self.balance += money
        return self.balance

    def withdraw(self, money):      #금액을 출금하는 함수
        if self.balance < money:    #계좌에 있는 돈보다 많은 금액을 출금할 시 0리턴
            return 0
        else:
            self.balance -= money   #계좌에 있는 돈보다 적은 금액을 출금할 시 정상 작동
            return money

    def getBalance(self):       #유저의 잔액을 리턴하는 함수
        return self.balance

class BankManager:
    # 출금처리를 담당할 메서드
    def withdraw(self, userid):
        for i in all_id:
            if i.getid() == userid:
                money = int(input("출금금액 = "))
                return i.withdraw(money)
        print("해당하는 계좌가 없습니다.")

    # 입금처리를 담당할 메서드
    def deposit(self, userid):
        for i in all_id:
            if i.getid() == userid:
                money = int(input("입금금액 = "))
                bal = i.deposit(money)
                print("잔액은 {0} 입니다.".format(bal))
                return 0
        print("일치하는 계좌번호가 존재하지 않습니다")

    # 계좌번호의 중복여부를 판단할 메서드
    def new_id(self, user):
        for i in all_id:
            if i.getid() == user.getid():
                return "입력하신 계좌번호는 이미 존재하는 계좌번호 입니다."

        all_id.append(user)
        return "계좌 개설이 완료되었습니다."

        # 전체고객의 계좌정보를 출력할 메서드

    def showAccount(self):
        if len(all_id) != 0:
            for i in range(0, len(all_id)):
                all_id[i].disp()
        else:
            print("보유한 계좌가 없습니다.")

    # 파일 저장 메서드
    def save(self):
        f = open(file, "w")
        for i in all_id:
            f.write(i.info())

        f.close()
