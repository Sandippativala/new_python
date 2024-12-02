# 11. retrieve academic record from file and compute CGPA. 

import sys

if len(sys.argv) < 2:
    print("use : python pro11.py a.txt")
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    sum_creadit = 0
    cp = 0
    for line in f:
        a = line.split()
        print(a)

        cp += float(a[1]) * float(a[2])

        sum_creadit += float(a[1])
    print("sum of(credits * points) :-",cp)
    print("Total Credit :- ",sum_creadit)

    cgpa = cp / sum_creadit
    print(f"CGPA :- {cgpa:.2f}")

