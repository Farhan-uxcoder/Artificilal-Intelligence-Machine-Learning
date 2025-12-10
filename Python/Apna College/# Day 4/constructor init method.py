#_init_method os called automatically
class student:
    def __init__(self,name,cgpa):                     #current instance of the class  or reference to the current object
        print("constructor was called...")
        self.name = name
        self.cgpa = cgpa


stu1 = student("Rahul",9)
stu2 = student("urvashi",9.3)


print(stu1.name)
print(stu2.name)