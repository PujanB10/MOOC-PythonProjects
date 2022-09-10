my_dict={}
while True:
    command=int(input("command (1 search, 2 add, 3 quit):"))
    if command==2:
        name=input("name:")
        number=input("number:")
        my_dict[name]=number
        print("ok!")

    if command==1:
        check_name=input("name:")
        if check_name not in my_dict:
            print("no number")
            continue
        print(my_dict[check_name])

    if command==3:
        break
print("quitting...")

