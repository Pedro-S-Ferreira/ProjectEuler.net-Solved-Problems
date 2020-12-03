def count_corners(dimention):
    squared = dimention**2
    return squared + squared-(dimention-1) + squared-2*(dimention-1) + squared-3*(dimention-1)

total = 1
start = 3

while start <= 1001:
    total += count_corners(start)
    start += 2

print("\nThe sume of the numbers on the diagonals in a 1001 by 1001 spiral is:", total)