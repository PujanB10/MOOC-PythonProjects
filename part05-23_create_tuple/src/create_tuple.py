def create_tuple(x: int,y: int,z: int):
    second=max(x,y,z)
    first=min(x,y,z)
    return(first,second,x+y+z)


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))