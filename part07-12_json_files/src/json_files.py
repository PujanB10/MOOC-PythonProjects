import json

def print_persons(filename: str):
    with open(filename) as new_file:
        data=new_file.read()
        courses=json.loads(data)
        for course in courses:
            hobbies = '(' + ', '.join(course['hobbies']) + ')'
            print(f'{course["name"]} {course["age"]} years {hobbies}')



if __name__ == "__main__":
    print_persons("file1.json")
