# Banking Application
Acntno=0
Cusname=" "
Bcode=" "
mobile=0
Bal=0
def CreateAccount():
    global Acntno
    global Cusname
    global Bcode
    global mobile
    global Bal
    acntno = int(input("Enter the account number"));
    Cusname = input("Enter the customer name")
    Bcode=input("Enter Branch code")
    mobile = int(input("Enter the mobile number"))
    Bal = int(input("Enter current Balance"))
def acountdetails():
    print("Account number:", Acntno)
    print("Customer name:", Cusname)
    print("Bcode:", Bcode)
    print(" Mobile number:", mobile)

def Deposit(amount):
    global Bal
    Bal = Bal+amount
    CheckBalance()
def Withdraw(amount):
    global Bal
    Bal = Bal-amount
    CheckBalance()
def CheckBalance():
    print("Current Balance", Bal)
#main#
Ch1='y'
while(Ch1=='y'):
    print ("1.Create Account \n 2.Withdraw \n 3.Deposit \n 4.Check Balance")
    ch=int(input("Select any option "))
    if(ch==1):
        CreateAccount()
    elif(ch==2):
        amnt=int(input("Enter the Amount to Withdraw"))
        Withdraw(amnt)
    elif(ch==3):
        amnt=int(input("Enter the Amount to Deposit"))
        Deposit(amnt)
    elif(ch==4):
        CheckBalance()
    else:
        print("please select any four options Available above")
    print("do you want to continue.. press y")
    ch1 = input()