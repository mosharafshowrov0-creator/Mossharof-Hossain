a = 15
b = 12

print(type(a))
print(type(b))

print(a + b)
print(a - b)
print(a * b)
print(a / b)

c = int(a / b)
print(c, type(c))

c = float(c)
print(c, type(c))

message = "The result of a divided by b is "
print(message + str(c))

print(a > b)
print(a == b)