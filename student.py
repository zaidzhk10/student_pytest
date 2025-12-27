def student_details(usn,name,divison,age):
    result = (
        f"Student usn: {usn}\n"
        f"Student Name: {name}\n"
        f"Divison: {divison}\n"
        f"Age: {age}\n"
    )
    return result

if __name__ == "__main__":
    usn= "306"
    name = "Zaid"
    divsion = "E"
    age = "19"
    print(student_details(usn,name,divsion,age))
