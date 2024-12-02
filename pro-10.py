#replace word

import sys

if len(sys.argv) < 4:
    print("use: python pro-10.py guj.txt old_word new_word")
    sys.exit(1)

old = sys.argv[2]
new = sys.argv[3]

with open(sys.argv[1],'r') as f:
    a = f.read()

r = a.replace(old,new)

with open(sys.argv[1],'w') as f:
    f.write(r)

print(r)