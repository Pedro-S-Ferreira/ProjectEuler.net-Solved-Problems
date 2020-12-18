import math

def check_prime(number):
	for div in range(2, int(math.sqrt(number) + 1)):
		if number % div == 0:
			return False
	return True

def list_to_int(list):
	number = ''
	for item in list:
		number += item
	return(int(number))

def check_circular(prime):
	prime = list(str(prime))
	length = len(prime)
	for x in range(length):
		prime.append(prime[0])
		prime.remove(prime[0])
		if not check_prime(list_to_int(prime)):
			return False
	return True

circ_list = []

for x in range(2, 1000000):
	if check_prime(x):
		if check_circular(x):
			circ_list.append(x)

print("The amount of circular primes below 1 million is:", len(circ_list))