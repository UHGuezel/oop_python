# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

'''
First Part

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    buddy = Car("blue", 20000)
    miles = Car("red", 30000)
    for car in (buddy, miles):
        print(f"The {car.color} car has {car.mileage:,} miles")
'''

'''
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"

class JackRusselTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

if __name__ == '__main__':
    bello = JackRusselTerrier("Bello", 7)
    russel = Dachshund("Jordan", 3)
    print(bello.speak("Grrr"))
    print(bello.speak())
    print(russel.speak("Woof"))
'''

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):
    def speak(self, sound = "Bark"):
        return super().speak(sound)

if __name__ == '__main__':
    bello = GoldenRetriever("Jack", 4)
    print(bello.speak("Woof!"))