class Bank:

    def openAccount(self,acno,cname,blanace):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("hello...",self.cname,",your account number",self.acno,"is opened with",self.balance,"rs. ")
    def deposite(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            self.needs=amount-self.balance
            print("sorry..,you need another",self.needs,"rs. to withdraw")
    def checkBalance(self):
        print("current balance: ",self.balance)

b1=Bank()
acno=int(input("enter account number : "))
cname=input("enter customer name : ")
balance=int(input("enter initial balance : "))

b1.openAccount(acno,cname,balance)

while True:

    print("******************************************************************")
    print("1. deposit")
    print("2. withdraw")
    print("3. check balance")
    print("4. exit")
    print("******************************************************************")

    choice=int(input("enter your choice :"))
    print("******************************************************************")

    if choice==1:
        amount=int(input("enter deposite amount: "))
        b1.deposite(amount)
        print("******************************************************************")
    elif choice==2:
        amonut=int(input("enter withdraw amonut : "))
        b1.withdraw(amount)
        print("******************************************************************")
    elif choice==3:
        b1.checkBalance()
        print("******************************************************************")
    else:
        print("good bye,thank you for usimg our service...")
        print("******************************************************************")
        break    
