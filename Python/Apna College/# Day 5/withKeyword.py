with open("sample.txt", "r") as file:
    content = file.read()
    print(content)


with open("sample.txt","w") as file:
    data = file.write("Hey moon ! this is the thing which is replaced ")