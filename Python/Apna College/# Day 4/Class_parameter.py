'''
The 1st parameter is cls
they can only access the class objects

we use decorater too
@classmethod

'''

class Laptop:
    memory_type ="SSD"
    
    def __init__(cls,memory,RAM):
        cls.memory = memory
        cls.RAM = RAM
    
    @classmethod # this changes the behaviour of the method like when we gv the @classmethod on top of any method  the entire becomes the class method
    def get_memoryType(cls):
        print(f"storage type =  {cls.memory_type} with the RAM of {cls.RAM}")
    
    
        
    def get_info(cls): # this is a instance method
        print(f"Laptop having the following specs \n Memory of {cls.memory} \n RAM of {cls.RAM} with the {cls.memory_type} ")
        

l1 = Laptop("256","16")

print(l1.get_memoryType())