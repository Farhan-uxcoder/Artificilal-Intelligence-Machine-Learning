'''
these are used when we want to use neighter instance nor class
there is no compulsary parameter
@staticmethod



'''

'''

There are Three types of methods are there i.e
1. Instace
2. Class
3.static


'''


''

class Laptop:
    memory_type ="SSD"
    
    def __init__(cls,memory,RAM):
        cls.memory = memory
        cls.RAM = RAM
    
    @classmethod           # this changes the behaviour of the method like when we gv the @classmethod on top of any method  the entire becomes the class method
    def get_memoryType(cls):
        print(f"storage type =  {cls.memory_type}")
    
    @staticmethod
    def cal_dicount(price,discount):
        final_price = price - (discount * price /100)
        print(f"final price {final_price}")
        
        
    
        
    def get_info(cls): # this is a instance method
        print(f"Laptop having the following specs \n Memory of {cls.memory} \n RAM of {cls.RAM} with the {cls.memory_type} ")
        

l1 = Laptop("256","16")
l1.cal_dicount(40_000,10)
print(l1.get_memoryType())