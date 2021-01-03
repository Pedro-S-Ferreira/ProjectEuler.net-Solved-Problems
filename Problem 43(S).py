import itertools

possible_pandigitals = list(itertools.permutations((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 10))
possible_pandigitals_final = []

for pandigital in possible_pandigitals:
    current_number = ""
    for number in pandigital:
        current_number += str(number)
    possible_pandigitals_final.append(int(current_number))

result = 0

print("got here")

for pandigital in possible_pandigitals_final:
    pandigital = str(pandigital)
    if len(pandigital) == 9:
        continue
    if int(pandigital[1] + pandigital[2] + pandigital[3]) % 2 == 0:
        if int(pandigital[2] + pandigital[3] + pandigital[4]) % 3 == 0:
            if int(pandigital[3] + pandigital[4] + pandigital[5]) % 5 == 0:
                if int(pandigital[4] + pandigital[5] + pandigital[6]) % 7 == 0:
                    if int(pandigital[5] + pandigital[6] + pandigital[7]) % 11 == 0:
                        if int(pandigital[6] + pandigital[7] + pandigital[8]) % 13 == 0:
                            if int(pandigital[7] + pandigital[8] + pandigital[9]) % 17 == 0:
                                result += int(pandigital)

print("The result is:", result)