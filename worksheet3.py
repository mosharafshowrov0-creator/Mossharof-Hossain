# ICT105 Worksheet 3 - All Tasks in One File

# -----------------------------
# Task 1: Student Course Enrollment
# -----------------------------
print("\n--- Task 1: Student Course Enrollment ---")

course_enrollments = {
    1001: ["CS101", "MATH101"],
    1002: ["CS101", "MATH102"],
    1003: ["CS202", "PHY101"]
}

for student_id, courses in course_enrollments.items():
    print("Student ID:", student_id, "Courses:", courses)


# -----------------------------
# Task 2: Class Schedule by Department
# -----------------------------
print("\n--- Task 2: Class Schedule by Department ---")

departments = {
    "Computer Science": [
        ("Computer Science", "CS101", "Introduction to Computer Science"),
        ("Computer Science", "CS202", "Data Structures")
    ],
    "Mathematics": [
        ("Mathematics", "MATH101", "Calculus I")
    ]
}

for dept, courses in departments.items():
    print("\nDepartment:", dept)
    for course in courses:
        print(course)


# -----------------------------
# Task 3: Lecturer Assignments
# -----------------------------
print("\n--- Task 3: Lecturer Assignments ---")

lecturer_assignments = {
    "Dr. Brown": ["CS101", "MATH102"],
    "Mr. Johnson": ["CS202"]
}

for lecturer, courses in lecturer_assignments.items():
    print("Lecturer:", lecturer)
    print("Courses:", courses)


# -----------------------------
# Task 4: User Input Loop
# -----------------------------
print("\n--- Task 4: User Input Loop ---")

students = []

while True:
    name = input("Enter student name or type exit: ")

    if name.lower() == "exit":
        break

    students.append(name)
    print(name, "added to class.")

print("Class list:", students)


# -----------------------------
# Task 5: Room Capacity Finder
# -----------------------------
print("\n--- Task 5: Room Capacity Finder ---")

rooms = {
    101: [15, "Ground Floor", "Building A"],
    103: [20, "Ground Floor", "Building A"],
    105: [25, "Ground Floor", "Building A"]
}

students_needed = int(input("Enter number of students: "))

for room, details in rooms.items():
    if details[0] >= students_needed:
        print("Room:", room)
        print("Capacity:", details[0])
        print("Location:", details[1], details[2])
        break


# -----------------------------
# Task 6(a): Exit Condition Loop
# -----------------------------
print("\n--- Task 6(a): Exit Condition Loop ---")

students = []

while True:
    name = input("Enter name or exit: ")

    if name.lower() == "exit":
        break

    students.append(name)

print("Students:", students)
print("Total:", len(students))


# -----------------------------
# Task 6(b): Active Variable Loop
# -----------------------------
print("\n--- Task 6(b): Active Variable Loop ---")

students = []
active = True

while active:
    name = input("Enter name or stop: ")

    if name.lower() == "stop":
        active = False
    else:
        students.append(name)

print("Students:", students)


# -----------------------------
# Task 6(c): Break on Capacity
# -----------------------------
print("\n--- Task 6(c): Break on Capacity ---")

students = []
max_cap = 3

while True:
    name = input("Enter name: ")
    students.append(name)

    if len(students) == max_cap:
        break

print("Students:", students)


# -----------------------------
# Task 7: Infinite Loop
# -----------------------------
print("\n--- Task 7: Infinite Loop ---")
print("Press CTRL + C to stop")

count = 0

while True:
    text = input("Enter text: ")
    count += 1
    print(text)
    print("Lines entered:", count)