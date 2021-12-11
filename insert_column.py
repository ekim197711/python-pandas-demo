import random

import pandas as pd
import numpy as np
print('BEGIN')
df = pd.read_csv('./spaceships.csv', index_col=0)
# print(df.head(10))
print(df.shape)
df.insert(2, "Crashes", df["Fuel"]/2, True)
# randoms = np.random.randint(2,10, len(df.index))
randoms = np.random.randint(2,10, df.shape[0])
df.insert(1, "Crew", randoms, True)
print(df.head(10))
print(df.shape)

print('END')
