#Python variables
a = 10

# data types
# the type of data which is we assign to the variable

# int - integer numbers
x = 100
print(type(x))

#float - decimal numbers
y = 12.4
print(type(y))
num = 2+3j
print(type(num)) #complex
num.imag #imaginary part
num.real #real part

#string - sequence of characters
z="farhan"
print(type(z))
print(z)

#lists - collection of items
list1 =[1,2,3,4,]
list1[1]=20
print(list1)
print(type(list1))

#tuple - collection of items which is immutable
tuple1 = (1,2,3)
print(tuple1)

# file pointers
x = open('variables.txt','w')
print(type(x))
x.write("BISMILLAH")
x.close()

(x,y,z) = (5,10.4,"faraah")
print(x,y,z)

#assigning value to multiple variables
a=b=c=1
print(a,b,c)

print(10//3) # just print the value that is in integer part like output of this is only 3 not 3.33
print(10%3) # modulus operator gives the remainder value like output of this is 1

x.write("This is the second adding thing to the files")
x.close