from os import listdir
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)

print(*listdir("opinions"), sep="\n")

product_id = input("Podaj kod produktu: ")

opinions = pd.read_json(f"./opinions/{product_id}.json")



# print(opinions.head())

# average_score = opinions['stars'].mean() nazwa kolumny z nawiasie kwadratowym musi być gdy mamy spacje w nazwie kolumny


average_score = opinions.stars.mean()

# stats_count = opinions.groupby('stars').count() nie działa, albo zwraca za dużo

stars_count = opinions.stars.value_counts().reindex(np.arange(0,5,0.5), fill_value= 0)
# fig, ax = plt.subplots()

stars_count.plot.bar() #ax to oś x
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.show()

# print(type(stats_count))

# opinions.pros = opinions.pros.replace(list(),None)
# pros_count= opinions.pros.notnull().count()
# rows_count = opinions.shape[0]


# print(rows_count,"=>",pros_count)
# print(opinions)