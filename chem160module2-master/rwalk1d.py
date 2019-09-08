from random import choice
trials=1000
steps=10000
gothome=0
for i in range(trials):
    point=0
    for step in range(steps):
        point+=choice((-1,1))
        if point==0:
            gothome+=1
            break
print("Fraction that got home=",gothome/trials)
#at trials 100, he gets a fraction of 1.000 (always makes it home)
#at trials 1000, he gets a fraction of .992 (decreases probability of making home)