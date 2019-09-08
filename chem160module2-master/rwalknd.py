from random import choice
dim=4
trials=100
steps=10000
gothome=0
for i in range(trials):
    point=[0]*dim
    for step in range(steps):
        for j in range(dim):
            point[j]+=choice((-1,1))
        if point.count(0)==dim:
            gothome+=1
            break
print("Fraction that got home=%f in %d dims" % (gothome/trials,dim))
#fraction that got home decreases, so no the random walker does not get home in all directions