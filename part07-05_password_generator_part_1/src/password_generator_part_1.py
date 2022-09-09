from string import ascii_lowercase
from random import choice
def generate_password(length : int):
    result_string=""
    for i in range(length):
        result_string+=choice(ascii_lowercase)
    return result_string
    





if __name__ == "__main__":
    for i in range(10):
        print(generate_password(2))