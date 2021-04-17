import math

prime_list = []
start = 1
not_found = True
prime_fact_list1 = [2]
prime_fact_list2 = [2]
prime_fact_list3 = [2]
prime_fact_list4 = [2]

def check_prime(n):
    for div in range(2, int(math.sqrt(n) + 1)):
        if n%div == 0:
            return False
    if not n in prime_list:
        prime_list.append(n)
    return True

def get_prime_factors(n):
    list_prime_factors = []
    divisible = True
    while divisible:
        for prime in prime_list:
            if prime > n:
                divisible = False
                break
            if n%prime == 0:
                if not prime in list_prime_factors:
                    list_prime_factors.append(prime)
                n /= prime
                break
    return list_prime_factors

while not_found:
    prime_fact_list4 = prime_fact_list3
    prime_fact_list3 = prime_fact_list2
    prime_fact_list2 = prime_fact_list1

    start += 1

    check_prime(start)
    prime_fact_list1 = get_prime_factors(start)

    if len(prime_fact_list1) == 4:
        if len(prime_fact_list2) == 4:
            if len(prime_fact_list3) == 4:
                if len(prime_fact_list4) == 4:
                    print(prime_fact_list1, prime_fact_list2, prime_fact_list3, prime_fact_list4)
                    not_found = False

print("The solution is:", start - 3)