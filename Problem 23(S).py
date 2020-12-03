def get_div(number):
    div_list = []
    for div in range(1, int(number / 2) + 1):
        if number % div == 0:
            div_list.append(div)
    return div_list

def check_abundant(number):
    if not number % 2 == 0 and not number % 3 == 0:
        return False
    sum_of_divs = 0
    for item in get_div(number):
        sum_of_divs += item
    if number < sum_of_divs:
        return True
    return False

abundant_list = []
abundant_sum_list = [0]*28123

for attempt in range(12, 28124):
    if check_abundant(attempt):
        abundant_list.append(attempt)

for x in abundant_list:
    for y in abundant_list:
        z = x + y
        if z < 28123:
            if abundant_sum_list[z] != z:
                abundant_sum_list[z] = z

total = 0

for i in range(0, len(abundant_sum_list)):
    if abundant_sum_list[i] == 0:
        total += i

print("\nThe result is: ", total)