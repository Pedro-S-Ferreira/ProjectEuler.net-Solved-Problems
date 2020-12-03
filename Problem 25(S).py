f1 = 1
f2 = 1
lenght_f1 = 0
lenght_f2 = 0
term = 2
longest = 0

def check_lenght(f):
    return len(str(f))

while True:
    f1 = f1 + f2
    term += 1
    lenght_f1 = check_lenght(f1)
    if longest < lenght_f1:
        longest = lenght_f1
        print(str(longest) + "/1000")
    if longest > 1000:
        print("F" + str(term) + ": ", f1)
        break
    
    f2 = f1 + f2
    term += 1
    lenght_f2 = check_lenght(f2)
    if longest < lenght_f2:
        longest = lenght_f2
        print(str(longest) + "/1000")
    if longest >= 1000:
        print("F" + str(term) + ": ", f2)
        break
