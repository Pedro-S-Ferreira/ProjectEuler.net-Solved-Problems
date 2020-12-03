import csv

with open("c:/Users/Pedro Ferreira/Documents/Python/Project Euler/problem22.txt", newline="") as n:
    reader = csv.reader(n)
    lNames = list(reader)

letter_values = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}

lNames = sorted(lNames[0])

print(lNames)

total_score = 0

def get_score(name):
    name_score = 0
    for letter in name:
        name_score += letter_values[letter]
    return name_score

for name in lNames:
    total_score += get_score(name) * (lNames.index(name) + 1)

assert (get_score("COLIN") == 53), "Colin's initial score isn't 53"
assert (get_score("COLIN") * (lNames.index("COLIN") + 1) == 49714), "Colin's initial score isn't 49714"

print("\nThe total score is: ", total_score)