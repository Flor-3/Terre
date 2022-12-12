import sys

if len(sys.argv) > 1:
    i = sys.argv[1]
    if i.isnumeric():  
        if int(i)%2 == 0:
            print('pair')
        elif int(i)%2 != 0:
            print('impair')
    elif i.isalpha():
        print('erreur')
    elif i[0] == '-':
        if int(i[1:])%2 == 0:
            print('pair')
        elif int(i[1:])%2 != 0:
            print('impair')
else:
    print('erreur')