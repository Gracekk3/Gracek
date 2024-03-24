students = [
    {"name": "Pepa", "age": 25, "major": "Ajták"},
    {"name": "Emma", "age": 23, "major": "Matematikářka"},
    {"name": "Michal", "age": 27, "major": "Inženýr"}
]


name_to_find = "Emma"
for student in students:
    if student["name"] == name_to_find:
        print("Informace o studentovi:", student)
        break
else:
    print("Student s jménem", name_to_find, "nebyl nalezen.")
