from cProfile import label

import matplotlib.pyplot as plt

x = [
    "januar",
    "februar",
    "mart",
    "april",
    "maj",
    "jun",
    "jul",
    "avgust",
    "septembar",
    "oktobar",
    "novembar",
    "decembar"
]
y_2024 = [23,31,27,35,22,26,19,24,18,30,25,33]
y_2025 = [12,18,10,25,19,30,22,27,20,35,28,40]

plt.plot(x, y_2024, label='2024', marker='o', color='red')
plt.plot(x, y_2025, label='2025', marker='s', color='green', linestyle='--')

plt.xlabel("Meseci u godini")
plt.ylabel("Broj ucenika tokom godine")
plt.title("Testovi i bodovi")
plt.grid()
plt.legend()

plt.annotate("Godisnji odmor",
             xy=("jul", 20),
             xytext=("jul", 25),
             arrowprops=dict(facecolor="black", shrink=0.25))

plt.scatter("jul", 20, s=100, zorder=5, color="black") # zorder je prioritet prikazivanja tacke (ako ih ima vise)

plt.show()