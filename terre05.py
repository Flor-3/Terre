import sys

a = int(sys.argv[1])
b= int(sys.argv[2])

if b == 0:
    print('erreur')
elif a//b == 0:
    print('erreur')
else:
    resultat = a//b
    reste = a%b
    print('résultat =', resultat)
    print('reste =', reste)