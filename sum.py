import pandas as pd

print('BEGIN')
df = pd.read_csv('./spaceships.csv', index_col=0)
print(df.head(10))
sum = df["Fuel"].sum(axis=1)
print(sum)

print('END')
