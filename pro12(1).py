# 12. use files to keep track of friend

import pro12 as f

while True:
    print("\n Friends Information")
    print("1. Add Friend")
    print("2. Remove Friend")
    print("3. Update Phone Num")
    print("4. Updata Github")
    print("5. printBYname")
    print("6. printALL")
    print("7. readALL")
    print("8. exit \n")

    choice = input("Enter your choice :-")

    if choice == "1":
        name = input("enter new friend name :- ")
        phone = input("enter phone number :- ")
        github = input("enter github :- ")
        f.add(name,phone,github)

    elif choice == "2":
        name = input("enter friend name :- ")
        f.remove(name)

    elif choice == "3":
        name = input("enter friend name :- ")
        phone = input("enter new phone :- ")
        f.updatephone(name,phone)

    elif choice == "4":
        name = input("enter friend name :-")
        github = input("enter new github :-")
        f.updategithub(name,github)
    
    elif choice == "5":
        name = input("enter friend name :- ")
        f.printbyname(name)

    elif choice == "6":
        f.printall()
    
    elif choice == "7":
        f.readall()

    elif choice == "8":
        print("Exit")
        break

    else:
        print("Invalid choice.") 