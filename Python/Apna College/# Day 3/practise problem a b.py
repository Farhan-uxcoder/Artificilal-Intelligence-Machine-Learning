info = [("alice","maths"),
        ("Navi","maths"),
        ("hela","english"),
        ("haan","science"),
        ("mathew","history"),
        ("sword","science")
        ]

#printing a unique course
unique_courses = set()
print("unique course is")
for tup in info :
    unique_courses.add(tup[1])
print(unique_courses)


# for name,course in info :
#     print(name,course)

#lists the students enrolled in english
for name,course in info:
    if(course=="english"):
        print(name)

#create a dictionary with the students with there sets of courses
dict = {}
for name,course in info:
    if dict.get(name==none):
