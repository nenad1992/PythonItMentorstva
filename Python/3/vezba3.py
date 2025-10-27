name = "marija"
password = "554321"

# Ako je ime admin i ako je sifra mojaSifra print ("Dobrodosao admine!")
# Ako je ime "toma" i ako je sifra "123456" print ("Dobrodosao Tomo")
# Alp je ime "marija" i ako je sifra "554321" print("Dobrodosla Marija")
# else print("Niste administrator! Pogresna sifra ili ime!")

if name == "admin" and password == "mojaSifra":
    print("Dobrodosao admine!")
elif name == "toma" and password == "123456":
    print("Dobrodosao Tomo!")
elif name == "marija" and password == "554321":
    print("Dobrodosla Marija!")
else:
    print("Niste administrator! Pogresna sifra ili ime!")