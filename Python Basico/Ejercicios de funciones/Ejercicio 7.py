def prime_check (number):
    is_prime = True
    for index in range(2,number):
        if number % index == 0:
            is_prime = False
            break
    return is_prime



def prime_extraction (number_list):
    prime_list = []
    for number in number_list:
        if prime_check(number) == True:
            prime_list.append(number)
    print(prime_list)

prime_extraction([1,4,6,7,13,9,67])
