class User:
    age = 0

john = User()
jessica = User()

john.age = 20
jessica.age = 35

print(john.age)
print(jessica.age)

def print_age(age):
    print("age:", age)
