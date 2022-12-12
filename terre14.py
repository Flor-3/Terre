import sys

if len(sys.argv) == 1:
    print('erreur')
    quit()
else:
    for i in sys.argv[1:]:
        if i.isalpha():
            print('erreur')
            quit()

intlist = sys.argv[1:]
if intlist == sorted(intlist):
    print('triée')
else:
    print('pas triée')