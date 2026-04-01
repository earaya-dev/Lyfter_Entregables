import random

user_number = int(input("Please, provide a number for prediction between 1 to 10"))
random_number = random.randint(1,10)

while (user_number != random_number):
        print("Wrong, try again")
        user_number = int(input("Enter your next number prediction between 1 and 10"))

print("Congratulations! You found the number.")
