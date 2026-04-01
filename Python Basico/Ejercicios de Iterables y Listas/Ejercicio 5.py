list1 = []

for numbers in range(10):
    enter_numbers = int(input("Enter a number,  10 times: "))
    list1.append(enter_numbers)
highest_number = max(list1)
print(list1 , f' The highest number was: {highest_number}')