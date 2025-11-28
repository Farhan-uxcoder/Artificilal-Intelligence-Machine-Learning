# dictionary is a unorderd collection of data in a key:value pair
# dictionaries are mutable
#for example the syntax of a dictionary is as follows
#varicle_name = {key1 : value1,key2 : value2......ken : valuen }

#declaring a empty dictionary
d1 = {}
print(d1)
print(type(d1)) #<class 'dict'>

#declaring a dictionary with some values
d2 = {1:"Welcome",2:"to",3:"python",4:"learning"}
print(d2) #{1: 'Welcome', 2: 'to', 3: 'python', 4: 'learning'}

#now the keys are defined as strings 
d3 = {"name":"Simplilearn","course":"python","duration":"3 months"}
print(d3) #{'name': 'Simplilearn', 'course': 'python', 'duration': '3 months'}

d4 = dict({1:"hello",2:"world"}) #using dict() function to declare a dictionary
print(d4) #{1: 'hello', 2: 'world'}

#using tuple
d5 = dict([(1,"hello"),(2,"farhan")])
print(d5)

#nested dictionary
d6 = {"name":{"first":"mohammed","last":"farhan"},"course":"python"}
print(d6)
