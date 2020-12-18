def check_no_0(num, den):
	if "0" in str(num) + str(den):
		return False
	return True

def check_non_trivial(num, den):
	result = num/den
	for number in str(num):
		if number in str(den):
			try:
				num -= int(number) * 10
				if num <= 0:
					num += int(number) * 10
					raise ValueError
			except:
				num -= int(number)
				num /= 10
			try:
				den -= int(number) * 10
				if den <= 0:
					den += int(number) * 10
					raise ValueError
			except:
				den -= int(number)
				den /= 10

			if result == num/den:
				return True

	return False

list_non_trivial = []

for den in range(99):
	for num in range(den - 1):
		if not num == den:
			if check_no_0(num, den):
				if check_non_trivial(num, den):
					list_non_trivial.append((num, den))

final_num = 1
final_den = 1

for item in list_non_trivial:
	final_num *= item[0]
	final_den *= item[1]

print(f"The product of the 4 fractions, given in its lowest common terms is: {1}/{int(final_den/final_num)}.")