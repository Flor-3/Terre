import sys

if len(sys.argv) == 1 or len(sys.argv) > 2:
    print('erreur')
elif str(sys.argv[1]).isnumeric():
    print('erreur')
else:
    print(len(sys.argv[1]))


