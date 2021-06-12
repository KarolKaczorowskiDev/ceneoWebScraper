from os import listdir
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


def convert_stars(stars):
    return float(stars.split("/")[0].replace(",","."))


pd.set_option("display.max_columns", None)

print(*[file_name.split(".")[0] for file_name in listdir("reviews")], sep="\n")
product_id=input("Podaj identyfikator produktu: ")

reviews = pd.read_json(f"reviews/{product_id}.json")

reviews.stars = reviews.stars.map (lambda stars : float(stars.split("/")[0].replace(",",".")))

reviews_count = len(reviews.index)

pros_count = reviews.pros.astype(bool).sum()

cons_count = reviews.cons.astype(bool).sum()
avarage_score= reviews.stars.mean().round(2)

stars = reviews.stars.value_counts(dropna= False).reindex(np.arange(0,5.01,0.5),fill_value=0)
stars.plot.bar(color="red")

plt.title ("Stars")
plt.xlabel ("Liczba gwiazdek")
plt.ylabel ("Liczba opinii")
plt.savefig(f"plots/{product_id}.png")
plt.close()