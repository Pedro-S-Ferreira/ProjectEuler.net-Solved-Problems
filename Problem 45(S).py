import math

def get_pentagonal(n):
    return int(n * (3 * n - 1) / 2)

def check_pentagonal(x):
    n = (math.sqrt(24*x+1)+1)/6
    if n.is_integer():
        return True
    return False

i = 1
not_found = True

while not_found:
    for ii in range(1, i):
        temp_i = get_pentagonal(i)
        temp_ii = get_pentagonal(ii)
        if check_pentagonal(temp_i+temp_ii):
            if check_pentagonal(temp_i-temp_ii):
                print("The solution is:", temp_i-temp_ii)
                not_found = False
    i+=1