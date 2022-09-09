def new_person(name: str, age: int):
    if len(name)==0 or len(name.split(" "))<2 or len(name)>40 or age<0 or age>150:
        raise ValueError("There was error in values.")
    else:
        return(name,age)

if __name__ == "__main__":
    print(new_person("Pujan Bhattarai",20))
