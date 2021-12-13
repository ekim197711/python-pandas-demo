import pandas as pd

print('BEGIN')
df = pd.read_csv('./spaceships.csv', index_col=0)
print(df.head(10))

print("COUNT --->")
# print(df.count())
# print(df.count(axis='columns'))

# print("Unique values ---> ")
# df_unique = df.value_counts("Captain")
# print(df_unique.describe())
# df_unique = df.value_counts("Captain")
df_unique = df.value_counts("Captain").rename_axis('unique_values').reset_index(name='valuecount')
# print(df_unique)
print(df_unique.loc[df_unique['valuecount'] > 3].head())
# print(df.loc[df['Fuel'] < 5].head())




print('END')
