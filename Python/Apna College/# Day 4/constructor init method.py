#_init_method os called automatically
class student:
    def __init__(self,name,cgpa):                   #current instance of the class
        print("constructor was called...")
        self.name = name
        self.cgpa


stu1 = student("Rahul",9)
stu1 = student("urvashi",9.3)
stu1 = student("shradha",9.5)

