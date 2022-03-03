class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
p = Point(2,8)
print(p.x)
print(p.y)
   
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        #creating list
        self.passengers = []
        
        
    def add_passenger(self, name):
        if not self.open_seats():
            self.passengers.append(name)
            
        return True
        
    def open_seats(self):
        return self.capacity-len(self.passengers)

Flight = Flight(3)

people = ["Harry", "Bobbyw", "Harmojnon"]

          