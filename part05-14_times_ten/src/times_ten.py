def times_ten(start_index,end_index):
    my_dict={}
    for i in range(start_index,end_index+1):
        my_dict[i]=i*10
    
    return my_dict

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)