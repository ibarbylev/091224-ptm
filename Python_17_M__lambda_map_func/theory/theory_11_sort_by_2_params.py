students = [
    ["John", "Doe", "Engineering", 21],
    ["Jane", "Smith", "Mathematics", 20],
    ["Dave", "Jones", "Engineering", 22],
    ["Eve", "Williams", "Mathematics", 21],
    ["Alice", "Brown", "Physics", 22]
]

sorted_students = sorted(students, key=lambda x: (x[3], x[2]))

for student in sorted_students:
    print(student)
