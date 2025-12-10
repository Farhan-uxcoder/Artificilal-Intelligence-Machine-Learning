#there are two types of constructors
#default constructors and parameteriesd constructor

class student:
    clg_name = "Acharya institute of technology"  #class attributes (default constructors are those which have the common value for all)

    def __init__(self,name,gpa,branch):
        self.name = name                          #method attributes
        self.branch = branch
        self.gpa = gpa


s1 = student("farhan",9.2,"ISE")
print(student.clg_name)
print(f"The student {s1.name} is studying in the {s1.branch} branch with the {s1.gpa} gpa")
