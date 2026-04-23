from abc import ABC, abstractmethod
import math

class BankAccount:
    def __init__ (self):
        self.balance = 0


    def deposit_money(self,deposit_amount):
        self.balance += deposit_amount


    def withdraw_money(self,withdraw_amount):
        self.balance -= withdraw_amount


class SavingsAccount(BankAccount):
    def __init__(self,min_balance):
        self.balance = 0
        self.min_balance = min_balance


    def check_min_balance(self,withdraw_amount):
        current_balance = self.balance - withdraw_amount
        if current_balance < self.min_balance:
            print("Error. Amount withdrawn cannot leave account's minimum balance below 5000 col.")




class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.pi = math.pi
        self.radius = radius

    def calculate_area(self):
        return self.pi * self.radius **2


    def calculate_perimeter(self):
        return  2 * self.pi * self.radius


        
class Square(Shape):
    def __init__(self, edge):
        self.edge = edge


    def calculate_area(self):
        return self.edge ** 2


    def calculate_perimeter(self):
        return  self.edge * 4


class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


    def calculate_perimeter(self):
        return  2 * (self.length + self.width)



## Herencia multiple use case

class Mother:
    def __init__(self):
        self.eye_color = "blue"
        self.skin_color = "white"

    def give_birth(self,pregnancy_time):
        if pregnancy_time >= 9:
            print("A baby has been born!")


class Father:
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "black"
    
    def pass_y_chromosome(self):
        print("Y chromosome has been passed from the father.")


class Baby(Father,Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)



## Bank account exercise calls ##

my_bank_account = BankAccount()
my_bank_account.deposit_money(15000)
my_bank_account.withdraw_money(11000)
print(f'My balance is: {my_bank_account.balance}')


my_savings_account = SavingsAccount(5000)
my_savings_account.deposit_money(20000)
my_savings_account.check_min_balance(4000)
my_savings_account.check_min_balance(25000)



## Shapes exercise calls ##
my_circle = Circle(6)
print(f'Circle Area: {my_circle.calculate_area()}')
print(f'Circle Perimeter: {my_circle.calculate_perimeter()}')

my_square = Square(4)
print(f'Square Area: {my_square.calculate_area()}')
print(f'Square Perimeter: {my_square.calculate_perimeter()}')

my_rectangle = Rectangle(8,10)
print(f'Rectangle Area: {my_rectangle.calculate_area()}')
print(f'Rectangle Perimeter: {my_rectangle.calculate_perimeter()}')



## Herencia multiple exercise calls ##

my_own_birth = Baby()     
print(f'I was born with eye color: {my_own_birth.eye_color}')
print(f'I was born with hair color: {my_own_birth.hair_color}')
my_own_birth.pass_y_chromosome()
print('I AM A BOY!!!!!!')  