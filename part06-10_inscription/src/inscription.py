name=input("Whom should I sign this to:")
file_name=input("Where shall I save it:")
with open(file_name,"w") as new_file:
    new_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")