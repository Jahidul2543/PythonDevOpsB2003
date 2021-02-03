class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "Dog {} age is {} which is a {}".format(philo.name, philo.age, philo.species)

    def speak(self, barking_sound):
        return "Dog barks {}".format(barking_sound)


# def demo(self):

philo = Dog("Philo", 6)
mikey = Dog("Mikey", 5)
print("Dog {} age is {} which is a {}".format(philo.name, philo.age, philo.species))

philo.speak("Woof Woof Woof")

