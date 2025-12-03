#sets are the collection of  unique elements
#in sets the elements cant be negative
s = {1,2,3,4,4,4,4,4}
print(s)
s.add(12)
print(s)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8,9}
print(s1.union(s2))
print(s1.intersection(s2))