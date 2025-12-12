#inheritence is the property of getting the functions and behaviour of one class to its subclass
print("Bismillah hir rahmanir rahim")

class Employee :
    start_time = "8:00 AM"
    end_time = "5:30 PM"
    
    def change_time(self,new_end_time):
        self.end_time = new_end_time
    
class Teacher(Employee):
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject
        
t1 = Teacher("Archana","Maths")
t1.change_time("6:45 PM")
print(f"The  teacher  {t1.name} takes subject {t1.subject} works till {t1.end_time}")

