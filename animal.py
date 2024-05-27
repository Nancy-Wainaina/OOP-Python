class Animal:
    def __init__(self,name):
        self.name = name
        
        
    def move(self):
        pass
    
    def make_noise(self):
        pass
    
    
class Cat(Animal):
    def move(self):
        print("The cat is walking")
        
        
    def make_noise(self):
        print("Meow")
        
        
class Bird(Animal):
    def move(self):
        print("The bird is flying")
        
    def make_noise(self):
        print("Chirp")
        
        
class Fish(Animal):
    def move(self):
        print("The fish is swimming")
        
    def make_noise(self):
        print("Boops")
        
        
        
c = Cat("Cat")
c.make_noise()
c.move()

b = Bird("Bird")
b.move()
b.make_noise()

f = Fish("Fish")
f.move()
f.make_noise()