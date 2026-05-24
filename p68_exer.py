student_marks={

"Jenny": 92,
"Harry":78,
"Dimpy":56,
"Rahul":41,

"Aniket":99,

"Prem":34

}
new=dict({})
for i in student_marks:
    if 91<student_marks[i]<100:
        student_marks[i]='A+'
    elif 81<student_marks[i]<90: 
        student_marks[i]='A'
    elif 71<student_marks[i]<80: 
        student_marks[i]='B'         
    elif 61<student_marks[i]<70: 
        student_marks[i]='C'     
    elif 41<student_marks[i]<60: 
        student_marks[i]='D' 

print(student_marks)











