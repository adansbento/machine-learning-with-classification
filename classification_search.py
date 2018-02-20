import pandas as pd

df = pd.read_csv('search.csv')

X_df = df[['home','search','login']]
Y_df = df['bought']

Xdummies_df = pd.get_dummies(X_df)
Ydummies_df = Y_df

X= Xdummies_df.values
Y= Ydummies_df.values

print(X)

print(Y)
