name = str(input("What's your name?"))
lastname = str(input("What's your last name?"))
age = int(input("What's your age?"))

if(age <= 2):
    print("You are a baby")
elif(age > 2 and age <= 9):
    print("You are a child" + "," + name , lastname)
elif(age >= 10 and age <= 12):
    print("You are a pre-adolescent" + "," + name , lastname)
elif(age >= 13 and age <= 18):
    print("You are a adolescent" + "," + name , lastname)
elif(age >= 19 and age <= 25):
    print("You are a young adult" + "," + name , lastname)
elif(age >= 26 and age <= 64):
    print("You are an adult" + "," + name , lastname)
else:
    print("You are a mature adult" + "," + name , lastname)
