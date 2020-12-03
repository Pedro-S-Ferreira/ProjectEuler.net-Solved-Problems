def how_many_collatz_steps(start_number):
    steps = 0
    while True:
        if start_number % 2 == 0:
            start_number = int(start_number / 2)
            steps += 1
            if start_number == 1:
                return steps
        else:
            start_number = 3 * start_number + 1
            steps += 1

highest = 0

for number in range(2, 1000001):
    if number % 10000 == 0:
        print(str(int(number / 10000)) + "/100")
    current = how_many_collatz_steps(number)
    if highest < current:
        highest_num = number
        highest = current

print("The number with the most steps is: ", highest_num)
