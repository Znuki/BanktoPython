import os  # loopy

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
      
try:
    f = open(file, "r")         #파이썬 파일을 연다

    while True:
        line = f.readline()     #파일을 읽는다
        if not line:
            break

        a, b, c = line.split(":")
        all_id.append(Account(a, b, int(c)))
    f.close()
except Exception as ex:         #파일이 없는 예외일 때 "파일 없습니다"를 출력
    print("파일 없습니다")
    print(ex)

# 화면 초기화
def clr():
    os.system('cls')            #시스템 명령어 호출


# 계좌정보를 이용하여 구현될 기능을 담고 있는 클래스 멤버필드 
# 멤버메서드 : makeAccount() - 계좌개설을 담당할 메서드

class BankManager:
    # 출금처리를 담당할 메서드
    def withdraw(self,userid):    
        for i in all_id:
            if i.getid() == userid:
                money = int(input("출금금액 = "))
                return i.withdraw(money)
        print("해당하는 계좌가 없습니다.")
        
    # 입금처리를 담당할 메서드
    def deposit(self,userid):     
        for i in all_id:
            if i.getid() == userid:
                money = int(input("입금금액 = "))
                bal = i.deposit(money)
                print("잔액은 {0} 입니다.".format(bal))
                return 0
        print("일치하는 계좌번호가 존재하지 않습니다")
    
    # 계좌번호의 중복여부를 판단할 메서드
    def new_id(self,user):             
        for i in all_id:
            if i.getid() == user.getid():
                return "입력하신 계좌번호는 이미 존재하는 계좌번호 입니다."
            
        all_id.append(user)
        return "계좌 개설이 완료되었습니다."   
    
    # 전체고객의 계좌정보를 출력할 메서드
    def showAccount(self):             
        if len(all_id) != 0:
            for i in range(0,len(all_id)):
                all_id[i].disp()
        else:
            print("보유한 계좌가 없습니다.")
                 
    # 파일 저장 메서드
    def save(self):
        f = open(file,"w")
        for i in all_id:
            f.write(i.info())
            
        f.close()
            
# 사용자와의 인터페이스를 담당할 목적의 클래스
class BanckingSystem: 
    def run():
        while True:
            print("==== Bank Menu ====")
            print("1. 계좌개설")
            print("2. 입금처리")
            print("3. 출금처리")
            print("4. 전체조회")
            print("5. 프로그램 종료")
            print("===================")
            choice = input("입력: ")
            if choice == "1":       # 계좌개설
                clr()
                print("=======계좌개설=======")
                print(BankManager().new_id(Account()))
                print("===================")
                
            elif choice == "2":     # 입금
                clr()
                print("========입 금========")
                userid = input("계좌번호 =")
                BankManager().deposit(userid)
                print("===================")
                 
                
            elif choice == "3":    # 출금
                clr()
                print("========출 금========")
                userid = input("계좌번호 =")
                a = BankManager().withdraw(userid)
                if a != None:
                    print("{0}원 출금하셨습니다.".format(a))
                
            elif choice == "4":    # 조회
                clr()
                print("========조 회========")
                BankManager().showAccount()
                print("===================")
                
            elif choice == "5":    # 종료
                BankManager().save()
                print("종료")
                break
                
            else:                # 예외처리
                print("잘못된 값을 입력했습니다.")
                

if __name__ =='__main__':
    BanckingSystem.run()        # 메인함수 실행
