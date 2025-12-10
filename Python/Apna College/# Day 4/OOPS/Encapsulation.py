class bankAccount :
    bankname = "SBI"
    
    def __init__(self,accName,accType,accBalance):
        self.accName = accName #public
        self._accType = accType #this is protected , by wrting the underscore '_' after dot '.'
        self.__accBalance = accBalance  #this is private coz of two underscore '__' after dot '.'
        
    def get_balance(self):
        return self.__accBalance
    
    def set_balance(self,newBalance):
        self.__accBalance = newBalance


b1 = bankAccount("Current","recuring",100_000)
print(b1.accName,b1.get_balance())

b2 = bankAccount("rahul","FD",123456)
b2.set_balance(54321)
print(f"the new balance of b2 is  {b2.get_balance()}" )


#print(f" the account name is {b1.accName} with the account type {b1._accType} the account balance is {b1.get_balance}")
#print(f"the account balance is {b1.__accBalance}") # this gvs the error coz we are trying to acces the private value
# to acces this private we have to use the getter and setter kind of functions

