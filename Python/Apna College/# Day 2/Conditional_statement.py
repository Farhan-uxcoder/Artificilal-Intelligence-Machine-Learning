age = int(input("enter the age "))

if age >= 18:
    print("can vote")
    print("Can drive")
else:
    print("wait for ",18-age," more years")

#for traffic light
color = input("enter the color of traffic light")
if color == "red":
    print("Stop")
elif color == "Orange":
    print("Ready")
elif color == "Green":
    print("GO!")
else:
    print("enter a valid color")
    



