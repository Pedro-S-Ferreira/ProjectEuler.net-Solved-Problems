total = 0

for x in range(1, 1000000, 2):
	bin_x = bin(x)[2:]
	if str(x) == str(x)[::-1]:
		if bin_x == bin_x[::-1]:
			total += x

print("The result is:", total)

print(bin(584)[2:] == bin(584)[2:][::-1])