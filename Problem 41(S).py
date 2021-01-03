import itertools, math

possible_pandigitals = list(itertools.permutations((1, 2, 3, 4, 5, 6, 7), 7))
possible_pandigitals.reverse()

def check_prime(number):
    for div in range(2, int(math.sqrt(number) + 1)):
        if number % div == 0:
            return False
    return True

found = False

while found == False:
    for pandigital in possible_pandigitals:
        current_number = ""
        for number in pandigital:
            current_number += str(number)
        print(current_number)
        if check_prime(int(current_number)):
            found = True
        if found == True:
            break

print("The highest pandigital prime is:", current_number)