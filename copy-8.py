#copy one file to another

import sys

if len(sys.argv) < 3:
    print("use: python copy-8.py myfile.txt myfile1.txt")
    sys.exit(1)

with open(sys.argv[1],'r') as f:
    with open(sys.argv[2],'w') as x:
        for line in f:
            x.write(line)

print("copy {0} to {1}".format(sys.argv[1],sys.argv[2]))