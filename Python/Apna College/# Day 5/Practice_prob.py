data = True
line = 1

with open("sample.txt","r") as f:
    while data:
        data = f.readline()
        if ("fine" in data):
            print(f"The word fine is found at the line {line}")
            break
        
        print(data)
        line+=1