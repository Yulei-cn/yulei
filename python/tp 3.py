'''
x=int(input("Entrez un nombre N : "))
i = 0
n = 0
while i < x:
    print(i)
    i += 1
    n=i+i
print("la somme des N entiers naturels %d" %n)

n=100
while True:
    x=int(input("Entrez un nombre N : "))
    if x == n:
        break

i=0
li=[]
while i < 10:
    i += 1
    a=int(input("10 valeur:"))
    if a > 0 and a <20:
       li.append(a)
    else:
        print("entre 0 et 20")
        i -= 1
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
    
x=int(input("donne la valeur:"))
i=0
n=0
a=0
while i < x:
    i += 1
    a=i-2
    n=i+i
    if n > x:
        print("alors le nombre N recherché est",a)
        break


import random
n=random.randint(1,100)
print(n)
while True:
    x=int(input("donne la valeur:"))
    if x<n:
        print("petit")
    else:
        if x>n:
            print("grand")
        else:
            print("egal")
            break

def func(n):
    res=n
    for i in range(1,n):
        res *= i
    return res


x=int(input("donnez la valeur:"))

print(func(x))

'''


