import math

def check_prime(number):
    for div in range(2, int(math.sqrt(number)) + 1):
        if number % div == 0:
            return False
    return True

counter = 0
counter_max = 0
result_a = 0
result_b = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        counter = 0
        checker = True
        while True:
            func_result = n**2 + a*n + b
            if func_result < 0:
                break
            if check_prime(func_result) == True:
                n += 1
                counter += 1
            else:
                break
        if counter > counter_max:
            counter_max = counter
            result_a = a
            result_b = b

print("\na is:", result_a)
print("b is:", result_b)
print("\nThe result of the product of a and b is:", result_a * result_b)