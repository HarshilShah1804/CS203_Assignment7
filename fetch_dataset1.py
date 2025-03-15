import pandas as pd
import os

if (os.path.exists("data") == False):
    os.mkdir("data")

train_data_url = "https://raw.githubusercontent.com/clairett/pytorch-sentiment-classification/master/data/SST2/train.tsv"
test_data_url = "https://raw.githubusercontent.com/clairett/pytorch-sentiment-classification/master/data/SST2/test.tsv"

train_df = pd.read_csv(train_data_url, delimiter='\t', header=None)
train_df.to_csv("data/dataset1.csv", index=False, header=False)

test_df = pd.read_csv(test_data_url, delimiter='\t', header=None)
test_df.to_csv("data/dataset1_test.csv", index=False, header=False)

url = "https://raw.githubusercontent.com/Ankit152/IMDB-sentiment-analysis/master/IMDB-Dataset.csv"
df_dataset = pd.read_csv(url, usecols=["review", "sentiment"])  
df_dataset.to_csv("data/dataset2.csv", index=False, header=True)