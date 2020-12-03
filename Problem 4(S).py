def check_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True

highest = 0

for val1 in range(1, 1000):
    for val2 in range(1, 1000):
        test = val1 * val2
        if check_palindrome(test) == True and test > highest:
            highest = test

print("The result is: ", highest)
