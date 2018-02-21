import pandas as pd

df = pd.read_csv('search.csv')

X_df = df[['home','search','login']]
Y_df = df['bought']

Xdummies_df = pd.get_dummies(X_df)
Ydummies_df = Y_df

X = Xdummies_df.values
Y = Ydummies_df.values

# perc/100
fit_size_percent = 0.01

fit_size = fit_size_percent * len(Y)
fit_data = X[:int(fit_size)]
fit_making = Y[:int(fit_size)]

test_size = len(Y) - fit_size
test_data = X[- int(test_size):]
test_making = Y[- int(test_size):]


from sklearn.naive_bayes import MultinomialNB

model1 = MultinomialNB()
model1.fit(fit_data,fit_making)

result = model1.predict(test_data)
diff = test_making - result

#Acertos hits
hits = [d for d in diff if d==0]
elements_amount = len(test_data)
hits_amount = len(hits)
hits_percent = 100.0*hits_amount/elements_amount

print 'Acertos/Total:',hits_amount,'/', elements_amount
print 'Acertos em %:',hits_percent
