def older_people(db:list, year: int):
    younger=[]
    for elements in db:
        if elements[1]<year:
            younger.append(elements[0])

    return younger

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    older = older_people(people, 1979)
    print(older)