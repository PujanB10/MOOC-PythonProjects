my_list=[]
while True:
    new_item=int(input("New item:"))
    if new_item==0:
        break
    my_list.append(new_item)
    print(f"The list now: {my_list}")
    print(f"The list in order: {sorted(my_list)}")
print("Bye!")