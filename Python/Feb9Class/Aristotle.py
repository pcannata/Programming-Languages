class Substance(object):
    def speak(self):
        raise NotImplementedError("Please Implement the speak method") # This is a way to do an abstract method.

class Quality:
    def __init__(self, courage = "Courage"):
        self.virtue = courage

class Animal(Substance, Quality):
    EYES = 11
    def __init__(self, name = 'Animal', virtue = "Courage"): # This is how to do Overloading in python.
        self.name = name
        self.virtue = virtue
    def speak(self):
        print "Animal says nothing."
    def haveSpeak(self, a): # This method will be used to demonstrate Polymophism.
        a.speak()

class Cat(Animal):
    def speak(self):
        print "Cat says Meow."

class Human(Animal):
    def __init__(self, sound = "I am a Human"):
        self.sound = sound
    def speak(self):
        print self.sound

a1 = Animal()
a2 = Animal()
c1 = Cat('myCat')
h1 = Human('Socrates')
h2 = Human("This human says something different")

a1.haveSpeak(a2)
a1.haveSpeak(c1)
a1.haveSpeak(h1)
a1.haveSpeak(h2)

print
print 'My name is: ', a1.name
print 'My virtue is: ', a1.virtue
print 'My name is: ', c1.name

