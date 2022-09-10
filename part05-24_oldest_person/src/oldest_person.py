def oldest_person(db: list):
    ref=db[0]
    smallest=ref[1]
    name=ref[0]
    for elements in db:
        if elements[1]<smallest:
            smallest=elements[1]
            name=elements[0]
    return name
        
if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))