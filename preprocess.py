import pandas as pd
import os

if (os.path.exists("data") == False):
    print("Dataset does not exists")

else:
    df2 = pd.read_csv("data/dataset2.csv", header=0)
    df2['sentiment'] = df2['sentiment'].map({'positive': 1, 'negative': 0})
    df2.to_csv("data/dataset2.csv", index=False, header=True)
    print("Preprocessing done")