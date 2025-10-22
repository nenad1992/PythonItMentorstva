# Napisati petlju koja ispisuje brojeve od 0 do 100
# Ispisati parne brojeve

# break za zaustavljanje petlje
# continue za preskakanje nekog naprajanja

# Preskoci broj 10
# A kod treba da stane kod broja 44

for number in range(100):
    if number == 10:
        continue

    if number == 44:
        break

    if number % 2 == 0:
        print(number)