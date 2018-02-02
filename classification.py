yes=1 
no=0

#      is fat? | has short leg? | do au au?
pig1 = [yes,yes,no]
pig2 = [no,yes,no]
pig3 = [no,no,no]

dog1 = [no,yes,yes]
dog2 = [no,yes,yes]
dog3 = [yes,yes,yes]

data = [pig1,pig2,pig3,dog1,dog2,dog3]

isPig = 1
isDog = -1

marking = [isPig,isPig,isPig,isDog,isDog,isDog]

# is fat? | has short leg? | do au au?
occult1 = [yes,yes,no]
occult2 = [yes,yes,yes]
occult3 = [yes,yes,no]

occults = [occult1,occult2,occult3]

from sklearn.naive_bayes import MultinomialNB

model1 = MultinomialNB()
model1.fit(data,marking)
marking_test = [ isPig,isDog,isDog]

result = model1.predict(occults)
diff = marking_test - result
hits = [d for d in diff if d==0]
elements_amount = len(occults)
hits_amount = len(hits)
hits_percent = 100.0*hits_amount/elements_amount

print 'Acertos/Total:',hits_amount,'/', elements_amount
print 'Acertos em %:',hits_percent
