triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

# Creating a list of lists, each corresponding to a row in the triangle
triangle_row = triangle.split("\n")
triangle_numbers = []
for row in triangle_row:
    triangle_numbers.append(row.split(" "))

# Code to print the entire triangle, each row in a line in terminal
for row in range(len(triangle_numbers)):
    print(triangle_numbers[row])

# Turning every item in the item into a integer instead of a string
for row in range(len(triangle_numbers)):
    for item in range(len(triangle_numbers[row])):
        triangle_numbers[row][item] = int(triangle_numbers[row][item])

while len(triangle_numbers) > 1:
    for row in range(2, 16):
        for number in range(len(triangle_numbers[-row])):
            triangle_numbers[-row][number] = max(triangle_numbers[-row][number] + triangle_numbers[-row + 1][number], triangle_numbers[-row][number] + triangle_numbers[-row + 1][number + 1])
    break

print("\nThe result is:", triangle_numbers[0][0])