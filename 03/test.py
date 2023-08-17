# Start the name of your classes with uppercase!

class User:
    age = 0

hiram = User()


lucy = User()

hiram.age = 33

print(hiram.age)
print(lucy.age)


class Monitor:
    width = 1080
    height = 720

monitor1 = Monitor()
monitor2 = Monitor()

monitor2.width = 1920

print(monitor1.width)
print(monitor2.width)


class Car:
    color = 'red'

car1 = Car()
car2 = Car()

car2.color = 'blue'

print(car1.color)
print(car2.color)
