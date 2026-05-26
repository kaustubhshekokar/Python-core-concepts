def new_student(name, roll_no, age, course):
    student_data = [
        {
            "name": "Ram",
            "roll_no": 10,
            "age": 33,
            "course": "Python",
        },
        {
            "name": "Kam",
            "roll_no": 13,
            "age": 23,
            "course": "C33",
        }
    ]

    new = {
        "name": name,
        "roll_no": roll_no,
        "age": age,
        "course": course
    }

    student_data.append(new)

    print(student_data)


name = input("Enter new name: ")
roll_no = int(input("Roll no: "))
age = int(input("Age: "))
course = input("Course: ")

new_student(name, roll_no, age, course)
