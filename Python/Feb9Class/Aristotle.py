class Animal(object):
    EYES = 2

    def __init__(self):
        self.legs = 4
    def speak(self):
        return "I am an animal"
    def makeSpeak(self, a):
        return a.speak()

print Animal.EYES

a1 = Animal()
print a1.legs
print a1.speak()

class Cat(Animal):
    def __init__(self):
        self.name = "Cat"
    def speak(self):
        return "I am a cat"

myCat = Cat()
a2 = Animal()

print "\nDemonstrating Polymorphsim"
print a1.makeSpeak(a2)
print a1.makeSpeak(myCat)



