class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.x = 11  # update for x value we can use that easily
print(point.x)  # 10
print()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"Hi,I am {self.name} and {self.age} years old")


jack = Person("Jack London", 30 )
# print(alex.name)
jack.talk()

alex = Person("Alex DESouza", 25)
alex.talk()
