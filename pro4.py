#Binary Search.

def binary(num):

    a = []

    for i in range(num):
        a.append(int(input("Enter {0} value: ".format(i+1))))

    a.sort()
    print(a)

    val = int(input("Enter value you want to search: "))

    low = 0
    high = num - 1
    found = False

    while low <= high:
        mid = low + (high - low) // 2
        if a[mid] == val:
            print(f"Value found at index: {mid}")
            found = True
            break
        elif a[mid] < val:
            low = mid + 1
        else:
            high = mid - 1

    if not found:
        print("Value not found in the list.")

num = int(input("Enter number of elements: "))
binary(num)
