def increment(number: int, by: int = 1) -> tuple:
    return (number, number + by)


print(increment(2, by=3))


def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


def save_user(**user):
    print(user)
    print(user["name"])


save_user(id=1, name="admin")


message = "a"

def greet():
  global message
  message = "b"

greet()
print(message)
