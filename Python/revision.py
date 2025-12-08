#finding a element in list
LS = [ 1,2,3,4,5]
index = 0
x = 3
for value in LS:
    if value==x:
        print(f"element found at {index+1} ")
        break
    index+=1

