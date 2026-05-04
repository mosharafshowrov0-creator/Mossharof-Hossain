# -------- LISTS --------

courses = [
    "Introduction to Programming", "Calculus I", "Data Structures and Algorithms",
    "Linear Algebra", "Physics I", "Chemistry I", "Biology I",
    "Microeconomics", "Macroeconomics", "Psychology I"
]

print(courses)

print(sorted(courses))
print(sorted(courses, reverse=True))

courses.reverse()
print(courses)

courses.sort()
print(courses)

courses.sort(reverse=True)
print(courses)


# -------- MODIFY LIST --------

courses.remove("Physics I")
courses.append("Discrete Mathematics")

courses.insert(0, "History I")
courses.insert(2, "English Composition I")
courses.append("Calculus II")

print(courses)

print("Removed:", courses.pop())
print("Removed:", courses.pop())
print("Removed:", courses.pop())
print("Removed:", courses.pop())

print(courses)


# -------- TUPLES + LOOP --------

course_tuples = [
    (1, "Intro to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures")
]

course_list = []

for cid, name in course_tuples:
    course_list.append(name)

print(course_list)


# -------- SEARCH SYSTEM --------

departments = [
    [1, "Computer Science"],
    [2, "Mathematics"],
    [3, "Computer Science"]
]

while True:
    user = input("Enter course ID (or quit): ")

    if user == "quit":
        break

    try:
        cid = int(user)
        found = False

        for item in departments:
            if item[0] == cid:
                print(item[1])
                found = True

        if not found:
            print("Not found")

    except:
        print("Invalid input")


# -------- COURSE INFO SYSTEM --------

courses_data = [
    [1, "Intro to Programming", "CS", "None"],
    [2, "Calculus I", "Math", "None"],
    [3, "Data Structures", "CS", "Intro to Programming"]
]

cid = int(input("Enter ID: "))

found = False

for c in courses_data:
    if c[0] == cid:
        print(c[1], c[2], c[3])
        found = True

if not found:
    print("Course not found")