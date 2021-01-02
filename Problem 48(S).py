total = 0

for x in range(1, 1001):
	total += x**x

print("The result is:", str(total)[-10:])