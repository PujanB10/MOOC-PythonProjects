def store_personal_data(person: tuple):
    with open("people.csv","a") as new_file:
        new_file.write(f"{person[0]};{person[1]};{person[2]}")






if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))
