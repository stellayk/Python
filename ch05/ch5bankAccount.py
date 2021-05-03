def bank_account(bal):
    balance = bal

    def getBalance():
        return balance
    def deposit(money):
        nonlocal balance
        balance += money
        print('After deposit of KRW %d your balance is KRW %d'%(money, balance))
    def withdraw(money):
        nonlocal balance
        if balance >= money:
            balance -= money
            print('After withdrawal of KRW %d your balance is KRW %d'%(money, balance))
        else:
            print("Insufficient balance.")
    return getBalance, deposit, withdraw


bal = int(input('Enter the initial balance of the account: '))
getBalance, deposit, withdraw = bank_account(bal)
print('The current balance is KRW',bal)

money = int(input('Enter the deposit amount: '))
deposit(money)
money = int(input('Enter the withdrawal amount: '))
withdraw(money)





