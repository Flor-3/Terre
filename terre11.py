import sys

nouvo = ''
minuit = ''
midi = ''

if 24 > int(sys.argv[1][0:2]) > 12:
    nouvo = sys.argv[1][0:2]
    nouvo = nouvo.replace(str(sys.argv[1][0:2]), str(int(sys.argv[1][0:2]) - 12))
    print(nouvo+sys.argv[1][2:5]+'PM')
elif 1 <= int(sys.argv[1][0:2]) <= 11:
    print(sys.argv[1]+'AM')
elif int(sys.argv[1][0:2]) == 00:
    minuit = sys.argv[1][0:2]
    minuit = minuit.replace(str(sys.argv[1][0:2]), str(int(sys.argv[1][0:2]) + 12))
    print(minuit+sys.argv[1][2:5]+'AM')
elif int(sys.argv[1][0:2]) == 12:
    midi = sys.argv[1][0:2]
    print(midi+sys.argv[1][2:5]+'PM')