class Account:
    __balance=0
    __accName=None
    __accNo=None

    def __init__(self, bal, name, no):
        self.__balance=bal
        self.__accName=name
        self.__accNo=no

    #Getter
    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo

    #Setter
    def deposit(self, money):
        if money<0:
            print('check balance')
            return
        self.__balance += money

    #Setter
    def withdraw(self, money):
        if self.balance < money:
            print('insufficient balance')
            return
        self.__balance -= money

#object
acc=Account(1000, 'John Smith', '123-456-7891-45')

#call getter
bal=acc.getBalance()
print('account info: ',bal)

#call setter
acc.deposit(10000)
bal=acc.getBalance()
print('account info: ',bal)