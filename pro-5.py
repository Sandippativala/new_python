import ad


while True:
    
    print("\nAcademic Performance")
    print("1. Add a course")
    print("2. Drop a course")
    print("3. Print academic record")
    print("4. Calaculate CGPA")
    print("5. Exit \n")
    
    choice = input("Enter your choice :-")
    
    if choice == "1":
        course_name = input("Enter course name :- ")
        credits = float(input("Enter course credits :- "))
        points = float(input("Enter earned points :- "))
        ad.add_course(course_name,credits,points)
    
    elif choice == "2":
        c_name = input("Enter course name to drop :-")
        ad.drop_course(c_name)
        
    elif choice == "3":
        ad.print_record()
        
    elif choice == "4":
        ad.cgpa()
           
    elif choice == "5":
        print("exit")
        break
    
    else:
        print("invalid choice :")
    