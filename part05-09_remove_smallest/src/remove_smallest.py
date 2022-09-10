def remove_smallest(my_list):
    smallest=min(my_list)
    my_list.remove(smallest)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)