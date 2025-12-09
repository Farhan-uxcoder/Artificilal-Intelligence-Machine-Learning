#finding a element in list
print("\n")

LS = [ 1,2,3,4,5]
index = 0
x = 3
print(LS)
for value in LS:
    if value==x:
        print(f"element found at {index+1} ")
        break
    index+=1

print("\n")

#tuple
tup = (1,2,3,4,5,6,7)
print(tup)
ind = 0
y = 4
for value in tup:
    if value == y:
        print(f"element found at {ind+1}th place")
        break
    ind+=1
    


#OOPS :Object oriented programming
#this means the mapping of the real world objects in the coding

class shelf:
    Genre = "Horror"
    pages = 120

print("\n")
s1 = shelf()
print(f"The Genre in the shelf is {s1.Genre}, and having the pages {s1.pages}")