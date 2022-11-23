li=[1,5,6,10,11,14,15,16,18,20]
i=0
n1=0
n2=0
n3=0
for i in li:
    if i < 10:
        n1 += 1
    else:
        if i >= 15:
            n3 += 1
        else:
            n2 += 1
print("Le nombre de valeurs inférieur strictement à ",n1,
    "\nLe nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15",n2,
    "\ni<=15",n3)
