def read_input(str,num1,num2):
    while True:
        try:
            num=int(input(str))
            if num1<num<num2:
                return num
        except ValueError:
            pass
        print(f"You must type in an integer between {num1} and {num2}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)