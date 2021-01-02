def check_right_angle(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    return False

def mn_to_abc(m, n):
    return m**2 - n**2, 2 * m * n, m**2 + n**2

list_solutions = []

for i in range(1001): #Getting all primitive triples using Euclid's formula <= 1000
    list_solutions.append([])
    if i == 0:
        continue
    for m in range(1, int(i/2) - 1):
        n = int(i / (2 * m) - m)
        if m > n and n > 0:
            a, b, c = mn_to_abc(m, n)
            if check_right_angle(a, b, c) and a + b + c == i:
                list_solutions[i].append((a, b, c))

for item in list_solutions: #Getting the remaining triples by using the primitive triples
    for abc in item:
        for i in range(1, 85): # 85 since 3x + 4x + 5x = 1000 => x = 83.3333 = 84
            try:
                new_a, new_b, new_c = abc[0] * i, abc[1] * i, abc[2] * i
                if new_a + new_b + new_c <= 1000:
                    if not (new_a, new_b, new_c) in list_solutions[new_a + new_b + new_c]: #This line stops most repeats but not all, as, for example, when p = 120, I get both (30, 40 50) and (40, 30, 50)
                        list_solutions[new_a + new_b + new_c].append((new_a, new_b, new_c))
                else:
                    break
            except:
                continue

for item in list_solutions: #Remove the final duplicates
    for abc in item:
        count = 0
        for i in range(len(item)):
            try:
                if abc[2] in item[i]:
                    count += 1
                    if count > 1:
                        item.remove(item[i])
            except:
                continue

maximised = [0, 0]

for i in range(len(list_solutions)): #Check for which value of p the number of solutions is maximised
    if len(list_solutions[i]) > maximised[0]:
        maximised[0], maximised[1] = len(list_solutions[i]), i

print("The value of p with the maximised number of solutions is", maximised[1], "with", maximised[0], "solutions.")