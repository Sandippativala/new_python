# print fibonacci sequence.

def fibonacci(n):

    a = "A"
    b = "B"

    for i in range(1,n +1):
        print(a,end=" ")
        sum = b + a
        a = b
        b = sum

n = int(input("enter number :-"))
if n <= 10:
    fibonacci(n)
else:
    print("please enter n less then 11")
