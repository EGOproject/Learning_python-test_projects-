class Point():
    def __init__(self, inputX, inputY):
        self.x = inputX
        self.y = inputY
    def __str__(self):
        return f"({self.x}, {self.y})"
p = Point(10, 2)
print(p)

#OOP

class Flight():
    def __init__(self, capacity):
        self.capacity=capacity
        self.passenger=[]

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passenger.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passenger)
    
flight = Flight(4)
people= ["dan", "rose", "mary", "enock", "fred", "bash"]
for person in people:
    if flight.add_passenger(people):
        print(f"{person} added to flight, vacant : {flight.capacity - len(flight.passenger)}")
    else:
        print(f"{person} missed! plane is at FULL CAPACITY")
# print(flight.passenger)


#decorators
def book(f):
    def wrapper():
        print("checking possible bookings")
        f()
        print("those are the results")
    return wrapper()

@book
def start():
    print("hello world")

#function lambda

people =[
    {"fname": "enock", "sname": "bbossa"},
    {"fname":"ben", "sname": "zziwa"},
    {"fname":"alex", "sname": "mwwanje"}
]
#either
def f(kid):
    return kid["fname"]
people.sort(key=f)
print(people)

#or
people.sort(key=lambda people: people["sname"])
print(people)

#try and except ...