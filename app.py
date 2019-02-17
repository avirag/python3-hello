# \"
# \'
# \\
# \n

course = "Python Programming"
len(course)
course[0]
course[-1]
course[0:3]
course[:3]
course[0:]
course[:]

print(id(course))
print(id(course[0]))

first = "John"
last = "Smith"
full = f"{first} {last}"
print(full)
test = f"{len(first)} {2 + 2}"
print(test)

print(course.upper())
print(course.lower())
print(course.title())

print(course.find('Pro'))
print(course.replace('P', '-'))
print("Programming" in course)
print("Programming" not in course)