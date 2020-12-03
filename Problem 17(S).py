def letter_counter(number):
    
    letters = 0
    units = 0
    dozens = 0
    hundreds = 0
    
    
    while number - 100 >= 0:
        hundreds += 1
        number -= 100
        
    while number - 10 >= 0:
        number -= 10
        dozens += 1
        
    units = number
    number = 0
    
    if hundreds > 0:
        letters += 7 #hundred
        
        if hundreds == 1 or hundreds == 2 or hundreds == 6:
            letters += 3
        if hundreds == 3 or hundreds == 7 or hundreds == 8:
            letters += 5
        if hundreds == 4 or hundreds == 5 or hundreds == 9:
            letters += 4
        
        if dozens > 0 or units > 0:
            letters += 3 #and

    if dozens == 2 or dozens == 3 or dozens == 8 or dozens == 9:
        letters += 6
    if dozens in range(4, 7):
        letters += 5
    if dozens == 7:
        letters += 7
        
    if dozens > 1 or dozens == 0:
        if units == 1 or units == 2 or units == 6:
            letters += 3
        if units == 3 or units == 7 or units == 8:
            letters += 5
        if units == 4 or units == 5 or units == 9:
            letters += 4
            
    elif dozens == 1:
        if units == 0:
            letters += 3
        if units == 1 or units == 2:
            letters += 6
        if units == 3 or units == 4 or units == 8 or units == 9:
            letters += 8
        if units == 5 or units == 6:
            letters += 7
        if units == 7:
            letters += 9
    
    return letters

total = 0

for nmb in range(1, 1000):
    total += letter_counter(nmb)

print("The sum is: ", total + 11) # adding " one thousand"
