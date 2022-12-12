import sys
from math import sqrt

if len(sys.argv) != 2:
    print('erreur')
elif sys.argv[1].isalpha():
    print('erreur')
else:
    print(int(sqrt(int(sys.argv[1]))))