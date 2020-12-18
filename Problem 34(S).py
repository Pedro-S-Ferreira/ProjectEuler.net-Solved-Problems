import math

final_total = 0

for i in range(10, 500000):
	total = 0
	for number in str(i):
		total += math.factorial(int(number))
	if i == total:
		final_total += i

print("The sum is: ", final_total)