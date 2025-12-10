class shop:
        def __init__(self,goods,price):
            self.goods = goods
            self.price = price

mannu = shop("oil",10)
print(mannu.goods)


class library:
    def __init__(self,bookname,bookid,reciver,submittedDate):
        self.bookname = bookname
        self.bookid = bookid
        self.reciver = reciver
        self.submittedDate = submittedDate

    def get_id(self):
       return self.bookid

b1 = library("java",45,"farhan",12)
b2 = library("python",35,"farhann",113)

print(b1.bookid,b1.reciver,b1.submittedDate,b1.bookname)
print(b2.get_id())


#for class of students
class students :
    def __init__(self,name,hobby,age):
        self.name = name
        self.age = age
        self.hobby = hobby

    def get_name(self):
        return self.name
    def get_hobby(self):
        return self.hobby
    def get_age(self):
        return self.age

s1 = students("meow","singing",12)
print(f"Name is {s1.get_name()}\nAge is {s1.get_age()} ")