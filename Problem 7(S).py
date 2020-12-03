p_list = []
start = 1
counter = 0

def check_prime(number):
    for item in p_list:
        if number % item == 0:
            return False
    p_list.append(number)
    return True

while counter != 10001:
    start += 1
    if check_prime(start) == True:
        counter += 1
        if counter % 1000 == 0:
            print(str(int(counter / 100)) + "%")

print("The 10001st prime is: ", start)
