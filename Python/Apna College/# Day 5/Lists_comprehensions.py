sq = []
for i in range (6):
    sq.append(i*i)
print(sq)

squre = [i*i for i in range(6)]
print(squre)

squre = [i*i for i in range(6) if((i%2)!=0)]
print(squre)