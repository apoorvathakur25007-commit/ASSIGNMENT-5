dict={"Oggy":78,"Nobita":47,"Shinchan":"99","Ninja Hatori":"39"}
name=input("Enter the student's name: ").title()
if name in dict.keys():
    for nm,val in dict.items():
        if nm==name:
            print(f"{name}'s marks: {val}")
else:
    print("Student not found.")