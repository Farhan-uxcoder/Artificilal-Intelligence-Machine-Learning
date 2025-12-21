# x = int(input("enter x:"))
# ans = 10/x
# print(ans)

#now lets write this using the exception handling

try:
    x = int(input("Enter x:"))
    ans = 10/x
except ZeroDivisionError:
    print("Division with zero is not possible")
except ValueError:
    print("enter a integer value")

else:
    print(ans)

finally:
    print("The code completed")
    