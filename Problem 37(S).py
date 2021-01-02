import math

def check_prime(number):
	number = int(number)
	if number == 1:
		return False
	for div in range(2, int(math.sqrt(number) + 1)):
		if number % div == 0:
			return False
	return True

counter = 0
current = 10
impossible_tuple = ("0", "4", "6", "8")
prime_list = [2, 3, 5, 7]
final_list = []

def reduce_left(number):
	return str(number)[1:]

def reduce_right(number):
	return str(number)[:-1]

while counter < 11:
	current += 1
	
	if any(x in impossible_tuple for x in str(current)):
		continue

	if check_prime(current):
		check_left = True
		check_right = True
		testing = current

		for i in range(len(str(current)) - 1):
			testing = reduce_left(testing)
			if not check_prime(testing):
				check_left = False
				break

		testing = current

		for i in range(len(str(current)) - 1):
			testing = reduce_right(testing)
			if not check_prime(testing):
				check_right = False
				break
		
		if check_left and check_right:
			final_list.append(current)
			counter += 1

print("The sum of all truncable primes is: ",sum(final_list))