def turn_into_triangle(x):
    return int(x * (x + 1) / 2)

def prime_factorisation(x, prime_list):
    prime_list = []
    while True:
        for prime in range(2, x + 1):
            if x % prime == 0:
                prime_list.append(prime)
                x = int(x/prime)
                break
        if x == 1:
            return prime_list
                
def calculate_divisor_amount(prime_list):
    divisor_list = []
    while not prime_list == []:
        for item in prime_list:
            divisor_list.append(prime_list.count(item) + 1)
            while item in prime_list:
                prime_list.remove(item)
    total = 1
    for item in divisor_list:
        total = total * item
    return total

start = 7
p_list = []
highest = 0

while True:
    start += 1
    if start % 2 == 0: #even; x/2 and x+1 
        prime1 = int(start / 2)
        prime2 = start + 1
        p_list = prime_factorisation(prime1, p_list) + prime_factorisation(prime2, p_list)
        divisors_amount = calculate_divisor_amount(p_list)
        if highest < divisors_amount:
            highest = divisors_amount
            print(str(highest) + "/500")

    elif highest > 500:
        break

    else: #odd; x and (x+1)/2
        prime1 = start
        prime2 = int((start + 1) / 2)
        p_list = prime_factorisation(prime1, p_list) + prime_factorisation(prime2, p_list)
        divisors_amount = calculate_divisor_amount(p_list)
        if highest < divisors_amount:
            highest = divisors_amount
            print(str(highest) + "/500")
            
    if highest > 500:
        break

print("\nNumber: ", start + 7)
print("The equivalent triangle number is (answer): ", turn_into_triangle(start))
