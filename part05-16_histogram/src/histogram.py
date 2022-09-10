def histogram(string):
    my_dict={}
    for characters in string:
        if not characters in my_dict:
            my_dict[characters]=0
        my_dict[characters]+=1
    for character,item in my_dict.items():
        stars="*"*item
        print(f"{character} {stars}")


if __name__ == "__main__":
    histogram("abba")
    