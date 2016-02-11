class Substance(object):
    def speak(self):
        raise NotImplementedError("Please Implement the speak method") # This is a way to do and abstract method

class Animal(Substance):
    EYES = 11
    def __init__(self):
        self.name = ''
    def speak(self):
        print "Animal says nothing."
    def haveSpeak(self, a):
        a.speak()

class Cat(Animal):
    def speak(self):
        print "Cat says Meow."

class Human(Animal):
    def __init__(self, sound = "I am a Human"): # This is how to do Overloading in python
        self.sound = sound
    def speak(self):
        print self.sound

a1 = Animal()
a2 = Animal()
c1 = Cat()
h1 = Human()
h2 = Human("This human says something different")

a1.haveSpeak(a2)
a1.haveSpeak(c1)
a1.haveSpeak(h1)
a1.haveSpeak(h2)

