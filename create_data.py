import random
import pandas as pd
import numpy as np
SHIP_FIRST=["Sky","Cloud","Quick"
    , "slow", "super", "overpowered"
    , "over","light","flash","lazer","cloak"
    ,"double", "power", "mc", "robo"]
SHIP_LAST=["bird", "angel", "falcon", "ship", "vessel", "transport","eagle","owl", "phantom","carrier","cruiser","freight"]
CAPTAIN_FIRST=["mike","rick", "susan", "katrine", "katia", "niels", "kåre", "thomas", "charlotte", "pernille"]
CAPTAIN_LAST=["dangerous","happy", "cute", "charming", "cowboy", "lazer", "lucky", "brain", "calm", "rich"]

def create_spaceship():
    mylist = []
    for x in range(0,100):
        # print("Create row")
        name = CAPTAIN_FIRST[random.randint(0,len(CAPTAIN_FIRST)-1)].capitalize()  + ' ' + CAPTAIN_LAST[random.randint(0, len(CAPTAIN_LAST) - 1)].capitalize()
        ship = SHIP_FIRST[random.randint(0,len(SHIP_FIRST)-1)].capitalize()   + SHIP_LAST[random.randint(0, len(SHIP_LAST) - 1)]
        fuel = random.randint(0,100)
        mylist.append([ship,name,fuel])
    return mylist



print('BEGIN')
df = pd.DataFrame(np.array(create_spaceship()),
                   columns=['Spaceship', 'Captain', 'Fuel'])
print(df.tail(15))
print(df.describe())
print(df.shape)
# df2.to_excel('./spaceships.xlsx')
df.to_html('./spaceships_2.html')
df.to_csv('./spaceships_2.csv')
print('END')
