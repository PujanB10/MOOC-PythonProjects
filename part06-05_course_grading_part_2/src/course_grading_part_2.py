if False:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_info=input("Exam points: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_info="exam_points1.csv"

name={}
with open(student_info) as new_file:
     for lines in new_file:
        lines = lines.replace("\n", "")
        list_of_name=lines.split(";")
        if list_of_name[0]=="id":
            continue
        name[list_of_name[0]]=list_of_name[1]+" "+list_of_name[2]

grades={}
with open(exercise_data) as new_files:
    for lines in new_files:
        sum=0
        lines = lines.replace("\n", "")
        list_of_ex=lines.split(";")
        if list_of_ex[0]=="id":
            continue
        for i in range(1,len(list_of_ex)):
            sum+=int(list_of_ex[i])
        perc=(sum/40)*100
        if perc<=10:
            grades[list_of_ex[0]]=0
        elif 20>perc>=10:
            grades[list_of_ex[0]]=1
        elif 30>perc>=20:
            grades[list_of_ex[0]]=2
        elif 40>perc>=30:
            grades[list_of_ex[0]]=3
        elif 50>perc>=40:
            grades[list_of_ex[0]]=4
        elif 60>perc>=50:
            grades[list_of_ex[0]]=5
        elif 70>perc>=60:
            grades[list_of_ex[0]]=6
        elif 80>perc>=70:
            grades[list_of_ex[0]]=7
        elif 90>perc>=80:
            grades[list_of_ex[0]]=8
        elif 100>perc>=90:
            grades[list_of_ex[0]]=9
        else:
            grades[list_of_ex[0]]=10
        

exam={}
with open(exam_info) as new_files1:
    for lines in new_files1:
        total=0
        lines = lines.replace("\n", "")
        list_exam=lines.split(";")
        if list_exam[0]=="id":
            continue
        for i in range(1,len(list_exam)):
            total+=int(list_exam[i])
        total+=grades[list_exam[0]]
        exam[list_exam[0]]=total



for elements in exam:
    if exam[elements]<=14:
        exam[elements]=0
    elif exam[elements]<=17:
        exam[elements]=1
    elif exam[elements]<=20:
        exam[elements]=2
    elif exam[elements]<=23:
        exam[elements]=3
    elif exam[elements]<=27:
        exam[elements]=4
    else:
        exam[elements]=5


for id,names in name.items():
    print(f"{name[id]} {exam[id]}")



        




