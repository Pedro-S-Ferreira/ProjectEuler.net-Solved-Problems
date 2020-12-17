import time

starttime = time.time()

def check_pandigital(mult1, mult2):
	res = mult1 * mult2
	if "0" in str(mult1) or "0" in str(mult2) or "0" in str(res):
		return False
	check = []
	if len(str(mult1)) + len(str(mult2)) + len(str(res)) == 9:
		for number in str(mult1) + str(mult2) + str(res):
			if not number in check:
				check.append(number)
			else:
				return False
	else:
		return False
	return res

list_results = []

for a in range(1, 9999):
	for b in range(a - 1, 9999):
		result = check_pandigital(a,b)
		if result:
			if not result in list_results:
				list_results.append(result)

print("The sum is:", sum(list_results), ". This code took ", time.time() - starttime, "seconds")