#functions are the block of code which are used to perform set of operations
#the function is defined by the "def"  keyword
def add(a,b):
    sum = a+b
    return sum

a = int(input("Enter the value of a:\t"))
b = int(input("Enter the value of b:\t"))
print("The sum of a and b is " , add(a,b))

