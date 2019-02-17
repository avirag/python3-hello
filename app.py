# immutable (bool, int, float, tuple, str, frozenset)
x = 1
print(id(x))
x = x + 1
print(id(x))

# mutable (list, set, dict)
y = [1, 2, 3]
print(id(y))
y.append(4)
print(id(y))