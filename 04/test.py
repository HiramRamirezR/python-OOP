class User:
    age = 0

john = User()
jessica = User()

john.age = 20
jessica.age = 35

print(jessica.age)
print(john.age)

def print_age(age):
    print("age:", age)
