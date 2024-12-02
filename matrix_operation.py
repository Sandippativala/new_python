matrixa = [[1, 2], [4, 5]]
matrixb = [[1, 2], [4, 5]]

def initialize_matrix():
    print("Fist Matrix")
    for i in range(2):
        for j in range(2):
            matrixa[i][j] = int(input("\nEnter value for a[{0}][{1}] :-".format(i,j)))
    
    print("Second Matrix")
    for i in range(2):
        for j in range(2):
            matrixb[i][j] = int(input("\nEnter value for b[{0}][{1}] :-".format(i,j)))

def print_matrix():
   print("First Matrix")
   for i in range(2):
        for j in range(2):
            print(matrixa[i][j],end = " ")
        print("\n")
   print("Second Matrix") 
   for i in range(2):
        for j in range(2):
            print(matrixb[i][j],end = " ")
        print("\n")

def addition_matrix():
    print("Addition of Matrix")
    for i in range(2):
        for j in range(2):
            print(matrixa[i][j] + matrixb[i][j], end=" ")
        print("\n")

def multipicaton_matrix():
    result = [[0,0],[0,0]]
    print("Multipicaton of Matrix")
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrixa[i][k] * matrixb[k][j]

    for row in result:
        print(row)
    print("\n")
multipicaton_matrix()