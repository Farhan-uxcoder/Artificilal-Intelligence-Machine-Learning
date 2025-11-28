#lists
# this are the collection of data of different data types

#creating a list

#for integers
num=[1,2,3,4]
print(num)

#for charecters
letters = ['a','b','c']
print(letters)

#for strings
strg = ["hello" , "world"]
print(strg)

#mix
mix = [ 1,'a',"hello"]

#list inside list
mat = [[1,2],['a','b']]
print(mat)

#accesing the elements in the list
print(mix[2])
print(mix[:2]) # output is 1 and a not hello

#every 2nd elements
print(mix[::2])

#reverse a list
print(mix[::-1])

#Operations on lists
z=[0] * 100
print(z)

#Concating
print(letters)
print(strg)
conc = letters + strg
print(conc)

#Unpacking 
var = list["hey there"]
print(var)

print(num)
one , *other = num
print(one)
print(other)

#Methods in lists

#Append
num.append(5)
print(num)

#Insert
num.insert(2,2.5)
print(num)

#Remove
num.remove(2.5)
print(num)

#pop
num.pop()
print(num)

#clear
num.clear()
print(num)

#length
print(len(letters))

#sort
unsorted = [3,1,4,2]
unsorted.sort()
print(unsorted)

#reverse
unsorted.reverse()
print(unsorted)

#copy
copylist = unsorted.copy()
print(copylist)

#count
print(unsorted.count(2))

#index
print(unsorted.index(4))

#extend
unsorted.extend([5,6,7])
print(unsorted)

#nesting tuples in list
mylist = [(1,2),(3,4),(5,6)]
print(mylist)

