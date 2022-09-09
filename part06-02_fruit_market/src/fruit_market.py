def read_fruits():
    dic={}
    with open("fruits.csv") as new_file:
        for line in new_file:
            parts = line.split(";")
            dic[parts[0]]=float(parts[1])
    return dic
if __name__ == "__main__":
    print(read_fruits())