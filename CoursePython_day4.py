import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [2, 4, 6, 8]
#
# plt.plot(x, y, label="Reeks 1")
# plt.title("Eenvoudige lijnplot")
# plt.xlabel("X-waarden")
# plt.ylabel("y-waarden")
# plt.grid(True)
# plt.legend()
# plt.show()

# data = {"Appels": 10, "Bananas": 15, "Cherries": 7}
# plt.bar(data.keys(), data.values())
# plt.title("Fruit per soort")
# plt.xlabel("Soort")
# plt.ylabel("Aantal")
# plt.show()


# x = [0, 1, 2, 3, 4]
# y1 = [0, 1, 4, 9, 16]
# y2 = [0, 1, 2, 3, 4]
#
# plt.style.use("ggplot")
# plt.plot(x, y1, marker="o", linestyle="--",
# label="kwadratisch")
# plt.plot(x, y2, marker="^", label="lineair")
# plt.xlim(0, 4); plt.ylim(0, 16)
# plt.title("Stijlen en opmaak")
# plt.xlabel("x"); plt.ylabel("y")
# plt.legend(); plt.grid(True)
# plt.show()




# x = [0, 1, 2, 3, 4]
# y1 = [n*n for n in x]
# y2 = [n*2 for n in x]
# fig, axes = plt.subplots(1, 2, figsize=(8, 3))
# axes[0].plot(x, y1);
# axes[0].set_title("Kwadratisch")
# axes[1].plot(x, y2, linestyle="--");
# axes[1].set_title("Lineair")
# fig.suptitle("Meerdere grafieken")
# plt.tight_layout(); plt.show()



#
# x = [1, 2, 3, 4, 5]
# y1 = [4, 2, 6, 8, 8]
# y2 = [3, 3.5, 6, 7, 4]
#
# plt.style.use("seaborn-v0_8")
# plt.plot(x, y1, label="Reeks 1", alpha=1)
# plt.plot(x, y2, label="Reeks 2", alpha=0.5)
# plt.title("Transparantie en stijl")
# plt.grid(True); plt.legend()
# plt.show()
# alpha is transparantie. 1 is niet transparant, 0.5 is half transparant.
# opslaan als .svg bestand, dan kan je de figuur open in je browser, en zo'n afbeelding is schaalbaar zonder de duidelijkheid te verliezen.




import csv
import pandas as pd

# dataset = read_csv_to_dict("Bestanden/Smartphone_Usage_Productivity_Dataset_50000.csv")
# print(dataset)

df = pd.read_csv("Bestanden/Smartphone_Usage_Productivity_Dataset_50000.csv")
plot_df = df[["Age", "Daily_Phone_Hours"]].dropna()

plt.figure(figsize=(8, 5))
plt.scatter(plot_df["Age"], plot_df["Daily_Phone_Hours"], alpha=0.7)
plt.title("Age vs Daily Phone Hours")
plt.xlabel("Age")
plt.ylabel("Daily_Phone_Hours")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Scatter plot:
# x = [1, 2, 3, 4, 5]
# y = [3, 3.5, 6, 7, 4]
#
# plt.scatter(x,y)
# plt.show()