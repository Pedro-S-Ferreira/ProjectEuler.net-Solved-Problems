def is_it_even(number):
    if number % 2 == 0:
        return True

value1 = 1
value2 = 1
total = 0

while value1 < 4000000 and value2 < 4000000:
    if value1 <= value2:
        value1 += value2
        if is_it_even(value1) == True:
            total += value1
    else:
        value2 += value1
        if is_it_even(value2) == True:
            total += value2

print("The result is: ", total)
