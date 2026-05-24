
student_data={
    "Ram":{"roll_no":10,"age":10,"course":"Python"},
    "Mohan":{"roll_no":20,"age":30,"course":"Python"},

}

print(student_data["Mohan"])
print(student_data["Mohan"]["roll_no"])

student_data["Mohan"]["phone_no"]=323443
print(student_data["Mohan"])

print(student_data["Mohan"].pop("phone_no"))

#so here we can nest list in dict dict in list like anything














