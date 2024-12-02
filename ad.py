course = ["bca"]
credits = [2]
earned_points = [2.7]

def add_course(course_name,credit,points):
    course.append(course_name)
    credits.append(credit)
    earned_points.append(points)
    
    print("course {0} add successfuly.".format(course_name))
    
def drop_course(course_name):
    found = 0
    for i in course:
        if i == course_name:
            course.remove(i)
            found = 1
            print("course {0} dropped successfuly.".format(course_name))
    if found == 0:    
        print("course {0} not found.".format(course_name)) 
    
def print_record():
    if not course:
        print("no course available.")
    else:
        print("    academic record: \n")
        for i,j,k in zip(course,credits,earned_points):
            print("academic course :-",i)
            print("total credits :-",j)
            print("earned points :-",k,"\n")
            
def cgpa():
    total_credits = 0
    for i in credits:
        total_credits = total_credits + i
    #print(total_credits)  
    
    if total_credits == 0:
        print("no courses available to calculate CGPA.") 
    else:
        mul = 1
        sum = 0 
        for i,j in zip(credits,earned_points): 
            mul = i*j
            sum = sum + mul
        CGPA = sum / total_credits
        print(f"current CGPA : {CGPA:.2f}")