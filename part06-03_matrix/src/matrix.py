def matrix_sum():
    sum=0
    with open("matrix.txt") as new_file:
        for line in new_file:
            parts=line.split(",")
            for elements in parts:
                sum+=int(elements)
    return sum



def matrix_max():
    max=0
    with open("matrix.txt") as new_file:
        for line in new_file:
            parts=line.split(",")
            for elements in parts:
                if int(elements)>max:
                    max=int(elements)

    return max


def row_sums():
    list_of_sum=[]
    with open("matrix.txt") as new_file:
        for line in new_file:
            sum=0
            parts=line.split(",")
            for elements in parts:
                sum+=int(elements)
            list_of_sum.append(sum)
    return list_of_sum




if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())
