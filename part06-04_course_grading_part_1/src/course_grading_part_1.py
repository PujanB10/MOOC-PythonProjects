if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

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
        grades[list_of_ex[0]]=sum

for id,names in name.items():
    if id in grades:
        print(f"{name[id]} {grades[id]}")        


        




