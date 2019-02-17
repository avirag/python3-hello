age = 22

# not, or, and
if not age <= 18:
  print('Hello')

if  18 < age < 70:
  print('John')

for x in "Python":
  print(x)

for x in ['a', 'b', 'c']:
  print(x)

for x in range(7, 15, 2):
  print(x)

print(type(range(5)))
print(type([1, 2, 3]))

names = ["John", "Mary"]
found = False
for name in names:
  if name.startswith("J"):
    print("Found")
    break
else:
  print("Not found")