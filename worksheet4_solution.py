# -------- FUNCTIONS --------

def course_enrollment(sid, fname, lname, cid, cname, action="Echo"):
    print(action, sid, fname, lname, cid, cname)

course_enrollment(1001, "Alice", "Smith", "CS101", "Intro")
course_enrollment(1002, "Bob", "Lee", "MATH101", "Calc", "Add")


# -------- COURSE LIST FUNCTION --------

def student_courses():
    courses = []
    for i in range(4):
        courses.append(input("Enter course: "))
    return courses

# print(student_courses())


# -------- DICTIONARY --------

def course_dict(**kwargs):
    return kwargs

print(course_dict(CS101="Intro", MATH101="Calc"))


# -------- SIMPLE CALCULATOR --------

import tkinter as tk

def calc():
    try:
        a = float(e1.get())
        b = float(e2.get())
        op = var.get()

        if op == "+":
            r = a + b
        elif op == "-":
            r = a - b
        elif op == "*":
            r = a * b
        else:
            r = a / b

        label.config(text=r)
    except:
        label.config(text="error")

root = tk.Tk()

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e1.pack()
e2.pack()

var = tk.StringVar(value="+")
tk.OptionMenu(root, var, "+", "-", "*", "/").pack()

tk.Button(root, text="=", command=calc).pack()
label = tk.Label(root)
label.pack()

# root.mainloop()


# -------- USER CLASS --------

class User:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.login_attempts = 0

    def greet(self):
        print("Hello", self.fname)

    def inc(self):
        self.login_attempts += 1

    def reset(self):
        self.login_attempts = 0

u = User("Alice", "Smith")
u.greet()
u.inc()
print(u.login_attempts)
u.reset()


# -------- CLASSROOM --------

class Classroom:
    def __init__(self, name, seats):
        self.name = name
        self.seats = seats
        self.students = 0

    def set_students(self, n):
        self.students = n

room = Classroom("Room1", 30)
room.set_students(20)
print(room.students)


# -------- INHERITANCE --------

class Equipment(Classroom):
    def __init__(self, name, seats):
        super().__init__(name, seats)
        self.devices = []

    def add(self, d):
        self.devices.append(d)

eq = Equipment("Room1", 30)
eq.add("Projector")
eq.add("Laptop")
print(eq.devices)