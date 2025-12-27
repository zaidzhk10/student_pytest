from student import student_details
def test_student():
    usn = "306"
    name = "Zaid"
    division = "E"
    age = "19"

    expected_output = (
        "Student USN: 306\n"
        "Student Name: Zaid\n"
        "Division: E\n"
        "Age: 19\n"
    )
    assert student_details(usn, name, division, age) == expected_output
