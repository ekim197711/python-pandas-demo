import pandas as pd

print('BEGIN')
df = pd.read_csv('./spaceships.csv', index_col=0)
# print(df.head(10))
# print("Type: " + str(type((False, True))))
df_sorted = df.sort_values(["Fuel", "Captain"], ascending=(False, True))
print(df_sorted.head(20))
print('END')
