list_prime_factors = []

number = 600851475143

while number != 1:
    for prime in range(2, number + 1):
        if number % prime == 0:
            number = int(number / prime)
            list_prime_factors.append(prime)
            break

print("The resul is: ", max(list_prime_factors))
