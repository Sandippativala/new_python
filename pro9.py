# 9. Write a programme to Split text into words and Join words to form sentences from one file to other file.

import sys

if len(sys.argv) < 3:
    print("use :python pro9.py myfile.txt myfile1.txt")
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    a = f.read().split()
    print(a)

with open(sys.argv[2],'w+') as x:
    for line in a:
        x.write(line + " ")
    x.seek(0)
    data = x.read()
    print(data)

print ("argv 1 is {0} and argv 2 is {1}".format(sys.argv[1],sys.argv[2]))

