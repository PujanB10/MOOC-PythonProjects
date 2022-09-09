import csv
from datetime import datetime, timedelta
def cheaters():
    start_date={}
    submission_time={}
    result=[]
    with open("start_times.csv") as read_start:
        for line in csv.reader(read_start, delimiter=";"):
            start_date[line[0]]=datetime.strptime(line[1],"%H:%M")
    
    with open("submissions.csv") as submission_file: 
        for line in csv.reader(submission_file, delimiter=";"):
            total_marks= int(line[1])+int(line[2])
            time_of=datetime.strptime(line[-1],"%H:%M")
            if line[0] in submission_time:
                if time_of > submission_time[line[0]]:
                     submission_time[line[0]] = time_of
            else:
                submission_time[line[0]]= time_of

    

    for elements in start_date:
        if submission_time[elements] - start_date[elements] > timedelta(hours=3):
            result.append(elements)

        
    return result

  
if __name__ == "__main__":
    print(cheaters())








