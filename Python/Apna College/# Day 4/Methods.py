'''

There are Three types of methods are there i.e
1. Instace
2. Class
3.static


'''



class Laptop:
    memory_type ="SSD"
    
    def __init__(self,memory,RAM):
        self.memory = memory
        self.RAM = RAM
        
    def get_info(self): # this is a instance method
        print(f"Laptop having the following specs \n Memory of {self.memory} \n RAM of {self.RAM} with the {self.memory_type} ")
        

l1 = Laptop("256","16")
l1.get_info()