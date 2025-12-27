def student_details(usn,name,divison,age):
    result = (
        f"Student usn: {usn}\n"
        f"Student Name: {name}\n"
        f"Divison: {divison}\n"
        f"Age: {age}\n"
    )
    return result

if __name__ == "__main__":
    usn = input("Enter Student USN: ")
    name = input("Enter Student Name: ")
    divison = input("Enter Division : ")
    age = input("Enter Student age: ")
    print(student_details(usn,name,divison,age))
