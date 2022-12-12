import sys

if len(sys.argv) == 1 or len(sys.argv) > 2:
    print('erreur')
else:
    if sys.argv[1].isalpha():
        print('erreur')
    elif int(sys.argv[1]) == 0 or int(sys.argv[1]) == 1:
        print('erreur')
    else:
        for i in range (int(sys.argv[1])):
            if i == 0 or i == 1:
                continue
            elif (int(sys.argv[1])%i == 0):
                print('Non, ' + sys.argv[1] + " n'est pas un nombre premier")
                break
            else:
                print('Oui, ' + sys.argv[1] + ' est un nombre premier')
                break