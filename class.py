class Animal:
    # Initialize method for constructor
    def __init__(self, name):
        self.name = name  # Instance attribute

    def speak(self):
        return f"{self.name} makes sound"


my_animal = Animal("Generic Animal")
print(my_animal.speak())

class Dog(Animal): #Dog inherits from Animal.
    def speak(self):
        return f"{self.name} barks!"

#Creating an instance of the subclass
my_dog = Dog("buddy")
print(my_dog.speak()) #Output: Buddy Barks.