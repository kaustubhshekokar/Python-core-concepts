def add_new_student(name,rollno, age, course_opted) :
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

    
    new_student={}
    new_student["Name"]=name
    new_student["roll_no"]=rollno
    new_student["age"]=age
    new_student["course"]=course_opted
    student_data.append(new_student)

    add_new_student("Shyam",22,18, "C++")
    print(student_data)
   