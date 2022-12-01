
'''
a=float(input("entrez une nomber:"))
i=1
j=0
tab=[]
for j in range (10):
    m =round(a*j)
    tab.append([a,j,m])
for i in tab:
    print(f"{i[0]} *{i[1]} = {i[2]}")




n = int(input("Donnez le nombre d'etudiants : "))
#人数
notes = []
list=[]
#创建一个主列表
moyenne = 0.0
x = 0
j=[]
for i in range(n):
    #j = []#创建新列表并添加到主序列表中
    #list.append(j)#将n个列表添加到主列表里面
    #j.append(x)
    #for i in range(1):
    a=int(input("Note etudiant %d : "%x))
    x=+1

    while 0>a or a>20:
        pass
        a=int(input("Note etudiant %d : "%x)) 

    
    #j.append(a)
    notes.append(a)
    moyenne = moyenne + a
moyenne= moyenne/n
print("Moyenne de classe : ",moyenne)

for i in range(n):
    #j=[]
    #j=list[i]
    
    
    print(f'{i}  | {notes[i]} | {notes[i] -moyenne}' )
    #moyenn = (notes[1]) -moyenne
    #list[i].append(moyenn)
    #i+=1


nMAX=10
v1=[]
v2=[]
while True:
    pscalaire=0.0
    n=int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ?"))
    m=int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ?"))

    if n>1 and n<=nMAX and m>=1 and m<=nMAX:
        print("Saisie du premier vecteur :")
        for i in range(0,n):
            v=float(input(f"v1[{i}]="))
            v1.append(v)

        print("Saisie du premier vecteur :")
        for i in range(0,m):
            x=float(input(f"v2[{i}]="))
            v2.append(x)

        if n==m:
            for r in range(0,n):
                pscalaire+=v1[r] * v2[r]
                r+=1
        else:
            v=n-m
            if v<0:
                for r in range(0,n):
                    pscalaire+=v1[r]*v2[r]
                    r+=1
            else:
                for r in range(0,n):
                    pscalaire+=v1[r]*v2[r]
                    r+=1

        print(f"\nLe produit scalaire de v1 par v2 vaut {pscalaire}")
        break
    else:
        continue
    '''
a = 5
b = 7
c = 30

test1 = (a * b - 30 > 0)
test = not((c % a == 0) or (a * b > 50)) or not test1
print(test)