start = 2520

while True:
    start += 20
    counter = 0
    for div in range(11, 21):
        if start % div == 0:
            counter += 1
        else:
            break
    if counter == 10:
        break

print("The result is: ", start)
