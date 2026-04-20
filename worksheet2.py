courses = [
    "Physics I",
    "Calculus I",
    "Biology I",
    "History I",
    "Psychology I"
]

print(courses)

print(sorted(courses))                 # alphabetical
print(sorted(courses, reverse=True))  # reverse alphabetical

courses.reverse()
print(courses)

courses.sort()
print(courses)

courses.sort(reverse=True)
print(courses)