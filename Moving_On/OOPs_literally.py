class BankAccount():
    import random
    defaultAccNumber = 1

    def __init__(self, name=input('Whats your name?\n'), balance=random.randint(1000,100000,)):
        self.name = name
        self.balance = balance
        self.accountNumber = BankAccount.defaultAccNumber
        BankAccount.defaultAccNumber = BankAccount.defaultAccNumber

    def StartUpGimmick(self):
        print("Initializing secure connection")
        from time import sleep
        sleep(1.5)
        for i in range(3):
            for j in range(i + 1):
                print('.', end=""), sleep(0.5)
            print(end=" ")
        print("\nHello, Welcome to Sim-Bank, Mr/Mrs", self.name)

    def deposit_module(self, amount=''):
        while True:
            qr = input("Would yu like to deposit?\n")
            if qr == '' or not qr[0].lower() in ['y','n',str]:
                print('HaHa Dont do that! Yes or No?')
            elif qr[0].lower() == 'y':
                amount = int(input("How much would you like to deposit?\n"))
                self.balance += amount
                print("New balance is $",self.balance)
                break
            else:
                break

    def view_Balance(self):
        while True:
            qr = input('Do you want to see current balance?\n ')  # qr stands for query jsky. \n supposed to receive input in nextline
            if qr == '' or not qr[0].lower() in ['y', 'n', str]:  # Will not accept answers not starting with 'y' or 'n'
                print('HaHa Dont do that! Yes or No?')
            elif qr[0].lower() == 'y':
                return self.balance
            else:
                break

    def withdraw(self):
        while True:
            qr = input("Would yu like to withdraw?\n")
            if qr == '' or not qr[0].lower() in ['y', 'n', str]:
                print('HaHa Dont do that! Yes or No?')
            elif qr[0].lower() == 'y':
                withdraw = int(input("How much would you like to withdraw?\n"))
                if self.balance < withdraw:
                    print('Insufficient Funds')
                else:
                    self.balance -= withdraw
                    print("New balance is $", self.balance)
                    break
            else:
                break

    def ClosingGimmick(self):
        print("Thank you for banking with Us")
        from time import sleep
        sleep(1.5)
        print("Buh-Bye")

while True:
    MyObj = BankAccount()
    MyObj.StartUpGimmick()
    print("Current bal $", MyObj.view_Balance())
    MyObj.deposit_module()
    MyObj.withdraw()
    MyObj.ClosingGimmick()
    import sys
    sys.exit()
