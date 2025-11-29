'''
there are two types of conversion

type conversion:
this is an implicit type conversion
which the interpreter does automatically
eg:
ans = 10.98 this is float
and when the int and float values are having operation we get the float values
because no data loss should happen

type casting:
this is an explicit type casting
for example when we change int to float we get as float but we dont want in float , we want in int
so we do this by using int()


'''

ans1 = int(5+10.0)
ans2 = 3+3.0
print(ans1,ans2)
print(type(ans1))
print(type(ans2))
