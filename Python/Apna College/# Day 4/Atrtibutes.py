#there are two types of attributes which are called as
'''
1} Class attributes (they belong to class) , common
2} Instance attributes (they belong to object) , different




'''

class student:                              #dekh yah kya horey so kato ab ik college mein sab student ke bhi clg ka name same hatey ny
    college = "ABC college"                 #ustey college name hame class attribute leti and woch ab har ik student ka name and USN df hatey ny so
    PI = 3.1                                #hame use object kako daal nah joki instance attributes hotey samjh ye yattach
    def __init__(self,name,USN):
        self.name = name
        self.USN = USN
        self.PI = 3.14
        
s1 = student("farhan",12345)
print(f"The student {s1.name} having USN {s1.USN} said the value of PI is {s1.PI}")