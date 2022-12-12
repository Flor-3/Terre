import sys

if len(sys.argv) != 3:
    print('erreur')
elif sys.argv[1].isalpha() or sys.argv[2].isalpha():
    print('erreur')
else:
    print(int(sys.argv[1]) ** int(sys.argv[2]))