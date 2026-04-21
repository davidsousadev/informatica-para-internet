import matplotlib.pyplot as plt
import numpy as np

brands = ["Apple","Dell","Lenovo","ASUS","Acer","Samsung","HP","MSI"]

# category scores (scaled to sum ~100)
reviews = np.array([20,20,18,18,17,17,15,17])
design = np.array([15,13,12,15,10,15,13,13])
support = np.array([13,15,13,12,10,10,12,10])
innovation = np.array([15,13,12,15,10,12,10,13])
value = np.array([12,13,15,13,17,13,13,12])
warranty = np.array([10,10,10,9,9,9,10,9])

categories = [reviews, design, support, innovation, value, warranty]
labels = ["Avaliações", "Design", "Suporte", "Inovação", "Custo-benefício", "Garantia"]

y = np.arange(len(brands))
left = np.zeros(len(brands))

plt.figure()

colors = ["#e57373","#ffb74d","#64b5f6","#fff176","#81c784","#ba68c8"]

for i, cat in enumerate(categories):
    plt.barh(y, cat, left=left, label=labels[i], color=colors[i])
    left += cat

# total score labels
for i, total in enumerate(left):
    plt.text(total + 1, i, f"{int(total)}", va='center')

plt.yticks(y, brands)
plt.xlabel("Pontuação (0–100)")
plt.title("Ranking de Marcas de Notebook (2026)")
plt.legend(loc="lower right")
plt.gca().invert_yaxis()

plt.show()