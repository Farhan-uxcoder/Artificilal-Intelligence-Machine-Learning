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

b1 = library("java",45,"farhan",12)
print(b1.bookid,b1.reciver,b1.submittedDate,b1.bookname)