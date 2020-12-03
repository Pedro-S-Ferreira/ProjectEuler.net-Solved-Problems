total100 = 1
result = 0

for x in range(1, 101):
    total100 *= x

for x in str(total100):
    result += int(x)

print("The sum of the digits of the result is: ", result)
