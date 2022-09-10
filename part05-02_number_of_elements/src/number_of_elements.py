def count_matching_elements(matrix,num):
    count=0
    for row in matrix:
        for element in row:
            if element==num:
                count+=1
    return count



if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))