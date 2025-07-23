class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.is_running = False
    
    def start(self):
        self.is_running = True
        return f"Engine started! {self.horsepower}HP {self.fuel_type} engine running"
    
    def stop(self):
        self.is_running = False
        return "Engine stopped"

class Transmission:
    def __init__(self, transmission_type):
        self.type = transmission_type
        self.current_gear = 1
    
    def shift_gear(self, gear):
        self.current_gear = gear
        return f"Shifted to gear {gear}"

class Car:
    def __init__(self, make, model, horsepower, fuel_type, transmission_type):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower, fuel_type)
        self.transmission = Transmission(transmission_type)
    
    def start_car(self):
        return self.engine.start()
    
    def drive(self, gear):
        if self.engine.is_running:
            return f"Driving {self.make} {self.model}. " + self.transmission.shift_gear(gear)
        return "Start the engine first!"

# Usage
car = Car("Toyota", "Camry", 268, "Gasoline", "Automatic")
print(car.start_car())  
print(car.drive(3))    
del car  