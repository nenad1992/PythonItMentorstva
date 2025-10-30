# Bubble Sort

# Uporedjuje
# Swap (menjanje mesta)
# Multiple Passes - radi sve dok ne zavrsi te prve 2 akcije

numbers = [5, 1, 4, 2, 8]

# Pass 1:
# Uporedjuje 5 i 1 -> 1, 5, 4, 2, 8

# for i in range(len(numbers)):
#     swapped = False
#     for j in range(0, len(numbers)-i-1):
#         if numbers[j] > numbers[j+1]:
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#             swapped = True
#     if not swapped:
#         break

for i in range(len(numbers)):
    for j in range(len(numbers)-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers)