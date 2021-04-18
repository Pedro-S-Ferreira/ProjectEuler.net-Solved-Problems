import math

def check_prime(n):
    for div in range(2, int(math.sqrt(n) + 1)):
        if n % div == 0:
            return False
    return True

'''What we know:
- Last digit of each prime must be 1, 3, 7 or 9
- They must increase by an even number
- The 3 primes must be between 1009 and 9973
- The theorical maximum increase is 4482
- The practical maximum increase is (last prime - first prime) / 2
- If we don't know any of the above values we can replace them by 1009 and 9973 respectively
- The sum of each individual number of each prime must be the same
'''

def check_valid(p1, p2, p3):
    for letter in p1:
        if not letter in p2 or not letter in p3:
            return False
    for letter in p2:
        if not letter in p1 or not letter in p3:
            return False
    for letter in p3:
        if not letter in p1 or not letter in p2:
            return False
    return True

not_found = True


for p1 in range(1009, 9974):
    if check_prime(p1):
        for increase in range(1, int((9973 - p1) / 2) + 1):
            if check_prime(p1 + increase):
                if check_prime(p1 + 2 * increase):
                    if check_valid(str(p1), str(p1 + increase), str(p1 + 2 * increase)):
                        result = [p1, p1 + increase, p1 + 2 * increase]
                        break

print("The result is:", result)