from random import sample
def lottery_numbers(amount: int, lower: int, upper: int):
    numbers=list(range(lower,upper))
    result=sample(numbers,amount)
    return sorted(result)




if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)