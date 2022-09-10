def input_points():
    result=""
    while True:
        numbers=input("Exam points and exercises completed:")
        if numbers=="":
            break
        result=f"{result} {numbers}"
    result=result.split(" ")
    result.pop(0)
    return result

def calculate_stats(data_given):
    total_points,num_of_exams=0,0
    for i in range(0,len(data_given),2):
        total=int(data_given[i])+int(data_given[i+1])//10
        if int(data_given[i])<10:
            grade0+=1
        elif total<=14:
            grade0+=1
        elif total<=17:
            grade1+=1
        elif total<=20:
            grade2+=1
        elif total<=23:
            grade3+=1
        elif total<=27:
            grade4+=1
        else:
            grade5+=1

        total_points+=total
        num_of_exams+=1
    grades=[grade0*"*",grade1*"*",grade2*"*",grade3*"*",grade4*"*",grade5*"*"]
    print("Statistics:")
    print(f"Points average: {total_points/num_of_exams:.1f}")
    print(f"Pass percentage: {(((num_of_exams)-grade0)/num_of_exams)*100:.1f}")
    print("Grade distribution:")

    for i in range(5,-1,-1):
        print(f"{i}: {grades[i]}")



        


data=input_points()
stats=calculate_stats(data)