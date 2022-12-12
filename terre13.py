import sys

if len(sys.argv) == 4:
    if sys.argv[1].isdigit() and sys.argv[2].isdigit() and sys.argv[3].isdigit():
        intlist = sys.argv[1:4]
        intlist.sort()
        print(intlist[1])
    else:
        print('erreur')
else:
    print('erreur')