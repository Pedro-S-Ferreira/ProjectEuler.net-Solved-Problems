irrational_fraction = "."
counter = 0

while len(irrational_fraction) < 1111111:
    counter += 1
    irrational_fraction += str(counter)

print("The result is:", int(irrational_fraction[1]) * int(irrational_fraction[10]) * int(irrational_fraction[100]) * int(irrational_fraction[1000]) * int(irrational_fraction[10000]) * int(irrational_fraction[100000]) * int(irrational_fraction[1000000]))