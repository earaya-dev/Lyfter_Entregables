def check_case (my_string):
    counter_lowercase = 0
    counter_uppercase = 0
    for each_letter in my_string:
        if each_letter.isupper():
            counter_uppercase += 1
            print(f'This is an upper case letter: {each_letter}')
        elif each_letter.islower():
            counter_lowercase += 1
            print(f'This is a lower case letter: {each_letter}')
    print(f'There is {counter_uppercase} uppercase characters and {counter_lowercase} lowercase characters in this string: {my_string}')

check_case("I Love Nacion Sushi")