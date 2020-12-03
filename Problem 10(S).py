import math

def check_prime(value):
	counter = 0
	for var in range(1, int(math.sqrt(value) + 1) + 1):
		if value % var == 0:
			counter += 1
	if counter > 1:
		return False
	else:
		return True
		
possibilities = list(range(2, 2000000))

print("Done")

for x in possibilities:
    print(possibilites[x - 1])
    if x % 2 == 0:
        possibilities.remove(x)
    if check_prime(possibilities[x]) == True:
        for y in possibilities:
            if y % possibilities[x] == True:
                possibilities.remove(y)

total_sum = 0

for z in possibilities:
    total_sum += possibilities[x]

print(total_sum)
