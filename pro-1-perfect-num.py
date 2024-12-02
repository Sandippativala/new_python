#find the perfect numbers

'''def pernum(num):
    number = []
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            number.append(i)
            print(i, end = "+")
            sum = sum + i
        
    if num == sum:
        print("\nnumber is perfect")
    else:
        print("\nnumber is not perfect")
    return sum


num = int(input("enter number :-"))
num1 = pernum(num)
print(num1)'''


def pernum(num):
    n = []
    sum = 0
    for i in range(1, num):
        if num % i == 0: 
            n.append(i)
            sum = sum + i 

    print(n)
       
    if sum == num:
        per.append(num)

per = []

ran = int(input("enter range :-"))
for num in range(1,ran):
    pernum(num)

if len(per) > 0:
    print("Perfect numbers between 1 to {0}:".format(ran), per)
else:
    print("perfect numbers between 1 to {0} not found".format(ran))
