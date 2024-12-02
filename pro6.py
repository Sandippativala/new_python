# 6 . Create a module for matrix operations.

import matrix_operation as mo

while True:
    print("\n Matrix Operations")
    print("1. Initialize Matrix")
    print("2. Print Matrix")
    print("3. Addition of Matrix")
    print("4. Multiplication of Matrix")
    print("5. Exit \n")

    choice = input("Enter your choice :-")

    if choice == "1":
        mo.initialize_matrix()

    elif choice == "2":
        mo.print_matrix()

    elif choice == "3":
        mo.addition_matrix()

    elif choice == "4":
        mo.multipicaton_matrix()
    
    elif choice == "5":
        print("Exit")
        break

    else:
        print("Invalid choice.")