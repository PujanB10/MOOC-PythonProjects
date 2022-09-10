def everything_reversed(list):
    new_list=[]
    for word in list:
        word=word[::-1]
        new_list.insert(0,word)
    return new_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    print(everything_reversed(my_list))