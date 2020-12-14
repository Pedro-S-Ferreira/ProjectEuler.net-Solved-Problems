coins = [0, 1, 2, 5, 10, 20, 50, 100, 200]
target = 20
combinations = [[1], [1], [1], [1], [1], [1], [1], [1], [1]]

for x in range(200):
    combinations[0].append(0)
for row in range(1, 9):
    for number in range(1, 201):
        combinations[row].append(number)

for x in range(8):
    combinations.append(combinations[1])

for row in range(1, len(coins)):
    coin = coins[row]
    for column in range(len(combinations[0])):
        if coin > column:
            combinations[row][column] = combinations[row - 1][column]
        else:
            combinations[row][column] = combinations[row - 1][column] + combinations[row][column - coin]

print("The total amount of possible combinations is:", combinations[8][200])

