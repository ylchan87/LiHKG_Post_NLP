import pandas as pd
from sklearn.model_selection import StratifiedKFold



df = pd.read_csv("./lihkg_posts_20190227.csv")

# split to train / test
spliter = StratifiedKFold(10, shuffle=True, random_state=0)
train_idx, test_idx = next(spliter.split(df, df['cat_id']))
df_train = df.iloc[train_idx]
df_test  = df.iloc[test_idx]

#futher split train to train/val
spliter = StratifiedKFold(10, shuffle=True, random_state=0)
train_idx, val_idx = next(spliter.split(df_train, df_train['cat_id']))
df_val   = df_train.iloc[val_idx]
df_train = df_train.iloc[train_idx]

#random order
def shuffle(df):
    return df.sample(frac=1).reset_index(drop=True)
df_train = shuffle(df_train)
df_val   = shuffle(df_val)
df_test  = shuffle(df_test)

df_train.to_csv("./lihkg_posts_20190227_train.csv", index=False)
df_val.to_csv("./lihkg_posts_20190227_val.csv", index=False)
df_test.to_csv("./lihkg_posts_20190227_test.csv", index=False)