import sys

myList = []
mystring = ''

if len(sys.argv) > 1:
    for element in sys.argv[1:]:
        myList.append(element + ' ')
    print(mystring.join(myList)[-2::-1])
else:
    print('erreur')