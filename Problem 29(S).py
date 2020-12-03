list_results = []

for a in range(2, 101):
    for b in range(2, 101):
        result = a**b
        if not result in list_results:
            list_results.append(result)

print("\nThe total amount of distinct items is:", len(list_results))