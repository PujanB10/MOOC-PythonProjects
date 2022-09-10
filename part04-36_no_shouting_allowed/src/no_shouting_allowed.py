def no_shouting(list):
    new_list=[]
    for element in list:
        if not element.isupper():
            new_list.append(element)

    return new_list
if __name__ == "__main__":
    my_list=["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized", "HELLO"]
    print(no_shouting(my_list))