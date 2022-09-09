from datetime import datetime
def is_it_valid(pic: str):
    if len(pic)!=11:
        return False
    check="0123456789ABCDEFHJKLMNPRSTUVWXY"
    keys={"+":1800, "-": 1900, "A": 2000}
    century=keys[pic[6]]
    year=century + int(pic[4:6])
    try:
        dob= datetime(year,int(pic[2:4]),int(pic[0:2]))
    except:
        return False
    control_character=int(pic[0:6]+pic[7:10]) % 31
    return check[control_character]==pic[10]
    
if __name__ == "__main__":
    print(is_it_valid("081842-720N"))