import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 9, 11]

plt.plot(x, y, color="red", marker="o")

for i in range(len(x)):
    plt.text(x[i], y[i], f'{y[i]}', ha='center', va='bottom')

plt.title("Wykres liniowy")
plt.xlabel("OŚ X")
plt.ylabel("OŚ Y")

plt.savefig('wykres.png')
plt.show()
