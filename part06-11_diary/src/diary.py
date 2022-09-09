def add_entry(string):
    with open("diary.txt","a") as new_file:
        new_file.write(string+"\n")


def read_entry():
    print("Entries:")
    with open("diary.txt") as new_file:
        for lines in new_file:
            print(lines.strip())

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function=input("Function:")
    if function=="1":
        text=input("Diary entry: ")
        add_entry(text)
        print("Diary saved")
    if function=="2":
        read_entry()
    if function=="0":
        print("Bye now!")
        break


