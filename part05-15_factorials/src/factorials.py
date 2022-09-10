def factorials(num):
    my_dict={}
    for i in range(1,num+1):
        fact=1
        for j in range(1,i+1):
            fact*=j
        my_dict[i]=fact
    return my_dict


if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])