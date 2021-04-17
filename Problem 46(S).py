import math

prime_list = [2]

def check_prime(n):
    for div in range(2, int(math.sqrt(n) + 1)):
        if n%div == 0:
            return False
    if not n in prime_list:
        prime_list.append(n)
    return True

def check_conjecture(start):
    for prime in prime_list:
        current_test = math.sqrt((start - prime)/2)
        if current_test == int(current_test)/1:
            return True
    return False

start = 1
not_found = True

while not_found:
    start += 2
    if not check_prime(start):
        if not check_conjecture(start):
            not_found = False

print("The result is:", start)