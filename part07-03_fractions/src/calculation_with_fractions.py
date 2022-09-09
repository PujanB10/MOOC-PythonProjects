from fractions import Fraction
def fractionate(amount: int):
    result=[]
    check=0
    while True:
        result.append(Fraction(1,amount))
        check+=Fraction(1,amount)
        if check==1:
            break
    return result
        



if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))