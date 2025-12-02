#Linear search
list = [1,2,3,4,5]
index = 0
x = 4
for value in list:
    if value==x:
        print(f"The element {x} found at the location {index+1}")
        break
    index +=1
