def largest():
    with open("numbers.txt") as new_file:
        maximum=0
        for line in new_file:
            line=int(line)
            if line>maximum:
                maximum=line
    return maximum

if __name__ == "__main__":
    print(largest())


