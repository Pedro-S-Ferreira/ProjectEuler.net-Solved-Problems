def sum_of_fifth(number):
    total = 0
    for val in str(number):
        total += int(val)**5
    if number == total:
        return True
    return False

'''
We start with the number 10 and go up from here as a sum must be involved. To find out the upper limit, we need to find out at which point
a number gets so big that even if all of its digits were 9, its fifth powers summed together would still be under the number it self.
We use this code to find that number:'''


limit = 2
while True:
    limit += 1
    if limit * (9 ** 5) < int(str(9) * limit):
        break

print(limit)
print(limit * 9 ** 5)

total = 0
count = 0

for x in range(10, int(limit * str(9)) + 1):
    if sum_of_fifth(x):
        count += 1
        total += x

print("\nThe total amount of a times a number is equal to the sum of the fifth of its individual numbers is: " + str(count) +"\nThe sum of those numbers is: " + str(total))