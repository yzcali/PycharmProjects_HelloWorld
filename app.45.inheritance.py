class Mammal:
    def walk(self):
        print("walk")

    def drink(self):
        print("milk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
dog1.walk()  # run programme and we see walk msg
dog1.bark()  # bark

cat1 = Cat()
cat1.be_annoying()  # annoying
cat1.drink()  # milk
