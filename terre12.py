import sys

strpm = ''

if sys.argv[1][5:7] == 'PM':
    if 1 <= int(sys.argv[1][0:2]) < 12:
        strpm = sys.argv[1][0:2]
        strpm = strpm.replace(strpm, str(int(strpm) + 12))
        print(strpm + sys.argv[1][2:5])
    else:
        print(sys.argv[1][0:5])
elif sys.argv[1][5:7] == 'AM':
    if sys.argv[1][0:2] == '12':
        print('00' + sys.argv[1][2:5])
    else:
        print(sys.argv[1][0:5])