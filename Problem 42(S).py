letter_to_numbers = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

fileopen = (open("C:/Users/Pedro Ferreira/Desktop/words.txt", "r"))
words = (fileopen.readline().replace('"','').split(","))

triangle_list = []
counter = 0

for n in range(1, 101): #Gettinga list of the first 100 triangle numbers so we can then check if each word's number is in that list.
    triangle_list.append(int(n * (n + 1) / 2))

for word in words:
    word_value = 0
    for letter in word:
        word_value += letter_to_numbers[letter]
    if word_value in triangle_list:
        counter += 1

print("From that file, there are", counter, "triangle words.")