from datas import load_access
from sklearn.naive_bayes import MultinomialNB
x,y = load_access()

fit_data = x[:90]
fit_making = y[:90]

test_data = x[-9:]
test_making = y[-9:]

model1 = MultinomialNB()
model1.fit(fit_data,fit_making)

result = model1.predict(test_data)
diff = test_making - result
hits = [d for d in diff if d==0]
elements_amount = len(test_data)
hits_amount = len(hits)
hits_percent = 100.0*hits_amount/elements_amount

print 'Acertos/Total:',hits_amount,'/', elements_amount
print 'Acertos em %:',hits_percent