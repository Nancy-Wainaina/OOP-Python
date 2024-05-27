class Vehicle:
        def __init__(self,make,model):
            self.make = make
            self.model = model
            
        def move(self):
            print("The vehicle is moving")
            
class Bus(Vehicle):
    def __init__(self,make,model,capacity):
                super().__init__(make,model)
                self.capacity = capacity
    def hoot(self):
        print("The bus is hooting")
    def check_capacity(self):
        print(f"The capacity is {self.capacity}")
        
        
class Lorry(Vehicle):
    def __init__(self,make,model,load_weight):
        super().__init__(make,model)
        self.load_weight = load_weight 
        
    def unload(self):
        print("Unloading the lorry") 
    def hoot(self):
        print("The lorry is hooting")
        
        
b = Bus ("x", "Isuzu", 70)
b.move()
b.hoot()
b.check_capacity()

l = Lorry("T", "Mercedez", 1000) 
l.move()
l.hoot()
l.unload()
             