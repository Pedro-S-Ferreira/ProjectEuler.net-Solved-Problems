def sum_divisors(number):
    total = 0
    for x in range(1, int(number / 2) + 1):
        if number % x == 0:
            total += x
    return total

list_numbers = list(range(1, 10001))
sum_under_10000 = 0

for item in list_numbers:
    if item == sum_divisors(sum_divisors(item)) and item != sum_divisors(item):
        print(sum_divisors(item))
        sum_under_10000 += item + sum_divisors(item)
        list_numbers.remove(sum_divisors(item))

print("\nThe sum of all amicable numbers under 10000 is: ", sum_under_10000)