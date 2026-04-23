class Circle:
    radius = 5

    def area():
        return 3.14 * Circle.radius ** 2
    

class Person():
	def __init__(self,current_bus_count):
		print(f'A person has mounted the bus. Current person count: {current_bus_count}')





class Bus():
    def __init__(self):
        self.max_passengers = 50
        self.passengers_in_the_bus = []
        self.current_bus_count = 0


    def add_passengers(self):
        while len(self.passengers_in_the_bus) < self.max_passengers:
            self.current_bus_count += 1
            self.passengers_in_the_bus.append(Person(self.current_bus_count))

    def unload_passengers(self):
        while len(self.passengers_in_the_bus) > 0:
            self.current_bus_count -= 1
            self.passengers_in_the_bus.pop()
            print(f"A person has left the bus. Current passengers on bus: {len(self.passengers_in_the_bus)}")


my_bus = Bus()
my_bus.add_passengers()
my_bus.unload_passengers()






class Head:
    def __init__(self):
        pass

class Torso:
    def __init__(self,head,right_arm,left_arm,right_leg,left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Arm:
    def __init__(self,hand):
        self.hand = hand

class Hand:
    def __init__(self):
        pass

class Leg:
    def __init__(self,feet):
        self.feet = feet

class Feet:
    def __init__(self):
        pass



class Human:
    def __init__(self):
        self.right_hand = Hand()
        self.left_hand = Hand()
        self.right_feet = Feet()
        self.left_feet = Feet()
        self.right_arm = Arm(self.right_hand)
        self.left_arm = Arm(self.left_hand)
        self.right_leg = Leg(self.right_feet)
        self.left_leg = Leg(self.left_feet)
        self.head = Head()
        self.torso = Torso(self.head, self.right_arm,self.left_arm,self.right_leg,self.left_leg)


person = Human()
print(f'This is a person: {person}')