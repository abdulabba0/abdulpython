"""
Encapsulation is a way of restricting access to some of the object's components.

Practise
Create a clas to simulate banking system, it should be able to register user, get account number, recieve deposit, withdraw, check account balance.

Account number
Account name
"""
# class BankAccount :
#     def __init__(self, account_number, account_holder_name, bvn):
#         self.__account_number = account_number
#         self.__account_holder_name = account_holder_name
#         self.bvn = bvn

#     def get_account_number(self):
#         return self.__account_number;

#     def update_account_number(self, account_number):
#         self.__account_number = account_number;
    

# class updateAcccount(BankAccount):
#     pass
    
# bank = BankAccount(1234567890, "John Doe", 1234567890)

# bank.update_account_number("4738473646834")
# print(bank.get_account_number())
# print(bank.__account_holder_name())
# print(bank.bvn())


class BankingSystem:
    def __init__(self, account_number, user_name, account_balance):
        self.__account_balance = 0
        self.register_user(account_number, user_name)
    
    def register_user(self, account_number, user_name):
        self.__account_number = account_number
        self.user_name = user_name

    def get_account_number(self):
        return self.__account_number

    def deposit(self, amount_to_deposit):
        self.__account_balance += amount_to_deposit
        # return f"Deposit of {amount_to_deposit} was successful"
    
    def check_balance(self):
        return self.__account_balance
    
    def withdraw(self, amount_to_withdraw):
        if amount_to_withdraw > self.__account_balance:
            return "Insufficient funds"
        self.__account_balance -= amount_to_withdraw
        return f"Withdrawal of {amount_to_withdraw} was successful"

bank = BankingSystem("1234567890", "John Doe", "2500")
print(bank.get_account_number())
bank.deposit(10000)
print(bank.check_balance())
bank.withdraw(2000)
print(f"Your Account Balance is : {bank.check_balance()}")