numbers = [0, 1]

while numbers[-1] < 100:
    next_number = numbers[-1] + numbers[-2]
    if next_number > 100:
        break
    numbers.append(next_number)


print(numbers)