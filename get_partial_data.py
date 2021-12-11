import pandas as pd


print('BEGIN')
df = pd.read_csv('./spaceships.csv', index_col=0)
print(df.head(3))

print("PARTIAL --->")
df_partial = df.loc[:,["Captain", "Fuel"]]
# df_partial = df.loc[df['Fuel'] < 20,["Spaceship", "Fuel"]]
# df_partial.loc[ :,["Captain", "Fuel"]] = ["Mike", 100]
print(df_partial.tail(100))




print('END')
