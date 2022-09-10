def add_student(db,name):
    db[name]=[]

def add_course(db,name,courses):
    if courses[1]>0:
        count=0
        copy=db[name][:]
        if db[name]==[]:
            db[name].append(courses)
        for elements in copy:
            if courses[0]==elements[0] and courses[1]>elements[1]:
                db[name].append(courses)
                db[name].remove(elements)
            if courses[0]!=elements[0]:
                count+=1
        if count==len(db[name]):
            db[name].append(courses)
 

def print_student(db,name):
    total_marks=0
    count=0
    if name not in db:
        print(name,end="")
        print(": no such person in the database")
    elif db[name]==[]:
        print(f"{name}:")
        print(" no completed courses")
    else:
        print(f"{name}:")
        print(f" {len(db[name])} completed courses:")
        for course in db[name]:
            print(f"  {course[0]} {course[1]}")
            total_marks+=course[1]
            count+=1
        print(f" average grade {total_marks/count}")

def summary(db):
    no_of_students=len(db)
    best_avg=0
    most=0
    person=""
    total_marks=0
    count=0
    for elements in db:
        if len(db[elements])>most:
            most=len(db[elements])
            persons=elements
        if db[elements]==[]:
            continue
        for element in db[elements]:
            total_marks+=element[1]
        avg=total_marks/len(db[elements])
        if avg>best_avg:
            best_avg=avg
            person=elements
        



    print(f"students {no_of_students}")
    print(f"most courses completed {most} {persons}")
    print(f"best average grade {best_avg} {person}")
            







if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    print_student(students,"Peter")
    print_student(students,"Emily")
    summary(students)
