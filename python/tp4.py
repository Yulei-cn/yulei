'''
a=int(input("entrez une nomber:"))
i=1
j=0
tab=[]
for j in range (10):
    m =a*j
    print('%d*%d=%d'%(a,j,m))
    tab.append('%d*%d=%d'%(a,j,m))
print(tab)
'''
nEs = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes=[]
numero=[]
n = 0.0
i=0
while i < nEs:
    numero.append(i)
    n=int(input("Note etudiant %d : "%i))
    i += 1
    notes.append(n)
notes=[['numero']]
print(notes)