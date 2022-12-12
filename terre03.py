import sys

lettre = sys.argv[1]
liste = []
chaine = ''

while ord(lettre) <= ord('z'):
    liste.append(lettre)
    lettre = chr(ord(lettre)+1)
    
print(chaine.join(liste)+'\n')