import pandas as pd
import csv

pokedex = pd.read_csv("pokemon_op.csv")
print(pokedex.head(5))

pokedex_1 = pokedex.drop(pokedex.columns[[0]], axis=1)

print(pokedex_1.head(5))

print(pokedex.dtypes)
print(pokedex_1.dtypes)

pokedex_1.to_csv(path_or_buf="pokemon_op_wo_row_id.csv", sep=';', header=True, decimal='.', mode='x', quotechar='"', index=False, quoting=csv.QUOTE_NONNUMERIC)