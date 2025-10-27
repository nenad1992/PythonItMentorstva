import platform
from platform import python_version

print(platform.system(), platform.platform(), platform.machine())

# Verzija pythona na mom racunaru je:
print(f"Verzija Python-a na mom racunaru je: {platform.python_version()}")

# Ako je verzija verzija Pythona koju koristimo veca ili manja od 3 (ako nije 3) onda ispisati poruku:
# Ne koristite dobru verziju Python-a

python_version = platform.python_version_tuple()

if int(python_version[0]) != 3:
    print("Ne koristite dobru verziju Python-a")
else:
    print("Koristite dobru verziju Python-a")