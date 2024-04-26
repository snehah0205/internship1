class Animal:
    def speak(self):
        return "animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "woof!"

class Cat(Animal):
    def speak(self):
        return "meow"
class Cow(Animal):
    pass


dog=Dog()
cat=Cat()
cow=Cow()

print("Dog says:",dog.speak())
print("Cat says:",cat.speak())
print("Cow says:",cow.speak())


