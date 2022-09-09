from datetime import datetime
day=int(input("Day: "))
month=int(input("Month: "))
year=int(input("Year: "))
yearold=datetime(1999,12,31)-datetime(year,month,day)
if yearold.days>0:
    print(f"You were {yearold.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")