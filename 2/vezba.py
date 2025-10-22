cars = ["Audi", "BMW", "Zastava"]

print(cars)

# BMW -> Mercedes

cars[1] = "Mercedes"

print(cars)

# Dadati jos 1 automobil na kraj "Skoda"
cars.append("Skoda")
print(cars)

# Sortirajte cars
cars.sort()
print(cars)

# Trenutno na stanju imamo X automobila
print(f"Trenutno na stanju imamo {len(cars)} automobila.")