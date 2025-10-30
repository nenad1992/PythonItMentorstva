# Linear Search
# Nadji najveci broj u listi
numbers = [3, 5, 2, 12, 8, 1]

max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number

print(max_number)

# Vezba: Pronaci broj 8
for number in numbers:
    if number == 8:
        print("Nasli smo broj 8")
        break

# Nadji koliko puta se ponavlja broj 8
# Nadji koliko puta se nesto povalja iz array
# Proveri duplikate