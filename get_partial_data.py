import pandas as pd


print('BEGIN')
df = pd.read_csv('./spaceships.csv', index_col=0)
df.loc[97,["Captain", "Fuel"]]=["Hello...1234",102]
print(df.tail(3))
print("PARTIAL --->")
# df_partial = df.loc[6:10,["Captain", "Fuel"]]
# df_partial = df.loc[df['Fuel'] < 20,["Spaceship", "Fuel"]]
# df_partial.loc[ :,["Captain", "Fuel"]] = ["Mike", 100]
# print(df_partial.tail(10))




print('END')
