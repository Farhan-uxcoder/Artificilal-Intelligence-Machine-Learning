class bankAccount :
    bankname = "SBI"
    
    def __init__(self,accName,accType,accBalance):
        self.accName = accName #public
        self._accType = accType #this is protected , by wrting the underscore '_' after dot '.'
        self.__accBalance = accBalance  #this is private coz of two underscore '__' after dot '.'
        
b1 = bankAccount("Current","recuring",100_000)
print(f" the account name is {b1.accName} with the account type {b1._accType} ")
print(f"the account balance is {b1.__accBalance}")
    