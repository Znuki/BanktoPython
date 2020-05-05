import os # loopy꺼
all_id = list() 

class Account:
    def __init__(self, userid= "", name = "", balance=0):    
        if(userid == ""):
            self.userid = input("계좌번호 = ")
            self.name = input("고객이름 = ")
            self.balance = int(input("예금금액 = "))
        else:
            self.userid = userid
            self.name = name
            self.balance = balance
            
    def disp(self):            
        print("계좌번호:{0}\t이름: {1}\t잔액: {2}".format(self.userid, self.name, self.balance))

    def info(self):
        return "{0}:{1}:{2}\n".format(self.userid, self.name, self.balance)
    

    def getid(self):
        return self.userid
    
    def deposit(self, money):
        self.balance += money
        return self.balance
    
    def withdraw(self, money):
        if self.balance < money:
            return 0
        else:
            self.balance -= money
            return money
    
    def getBalance(self):     
        return self.balance
                
try:
    f = open(file,"r")
    
    while True:
        line = f.readline()
        if not line:
            break

        a,b,c = line.split(":")
        all_id.append(Account(a,b,int(c)))
    f.close()
except Exception as ex:
    print("파일 없습니다")
    print(ex)
                
def clr():
    os.system('cls')
    
class BankManager:
    def withdraw(self,userid):    
        for i in all_id:
            if i.getid() == userid:
                money = int(input("출금금액 = "))
                return i.withdraw(money)
        print("해당하는 계좌가 없습니다.")
        
    def deposit(self,userid):     
        for i in all_id:
            if i.getid() == userid:
                money = int(input("입금금액 = "))
                bal = i.deposit(money)
                print("잔액은 {0} 입니다.".format(bal))
                return 0
        print("일치하는 계좌번호가 존재하지 않습니다")
    
    def new_id(self,user):             
        for i in all_id:
            if i.getid() == user.getid():
                return "입력하신 계좌번호는 이미 존재하는 계좌번호 입니다."
            
        all_id.append(user)
        return "계좌 개설이 완료되었습니다."   
    
    def showAccount(self):             
        if len(all_id) != 0:
            for i in range(0,len(all_id)):
                all_id[i].disp()
        else:
            print("보유한 계좌가 없습니다.")
                 
    def save(self):
        f = open(file,"w")
        for i in all_id:
            f.write(i.info())
            
        f.close()

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
            cho = input("입력: ")
            if cho == "1":       # 계좌개설
                clr()
                print("=======계좌개설=======")
                print(BankManager().new_id(Account()))
                print("===================")
                
            elif cho == "2":     # 입금
                clr()
                print("========입 금========")
                userid = input("계좌번호 =")
                BankManager().deposit(userid)
                print("===================")
                 
                
            elif cho == "3":    # 출금
                clr()
                print("========출 금========")
                userid = input("계좌번호 =")
                a = BankManager().withdraw(userid)
                if a != None:
                    print("{0}원 출금하셨습니다.".format(a))
                
            elif cho == "4":
                clr()
                print("========조 회========")
                BankManager().showAccount()
                print("===================")
                
            elif cho == "5":
                BankManager().save()
                print("종료")
                break

##############################
if __name__ =='__main__':
    BanckingSystem.run()