class Person:
    description = "general description"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "My name is {} I am {} years old".format(self.name, self.age)

    def eat(self, food):
        print("{} eats {}".format(self.name, food))


class Baby(Person):
    description = "Baby"

    def speak(self):
        print("Ba babababa")

    def nap(self):
        print("Baby name: {}".format(self.name))


person = Person("John", 40)
person.eat("Burger")
baby = Baby('Ini', 2)
baby.nap()
baby.eat('Baby food')