def check_pandigital(number):
    number = str(number)
    if len(number) == 9 and "0" not in number:
        for char in number:
            number = number.replace(char, "", 1)
            if char in number:
                return False
        return True
    else:
        return False

def create_final(temp_list):
    final = ""
    for item in temp_list:
        final += str(item)
    return final

list2 = [1]
current_highest = 0

for i in range(2, 10):

    list2.append(i)

    for j in range(1, 10000):
        temp_list = []
        for mult in list2:
            temp_result = mult * j
            if temp_result > 987654321:
                break
            else:
                temp_list.append(mult * j)
    
        final = int(create_final(temp_list))
        if final > current_highest and check_pandigital(final):
            current_highest = final

print("The largest pandigital is:", current_highest)