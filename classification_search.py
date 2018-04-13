import pandas as pd
from collections import Counter
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import MultinomialNB


def load_data(pathFile,fields,whatVar):
    
    df = pd.read_csv(pathFile)

    X_df = df[fields]
    Y_df = df[whatVar]

    Xdummies_df = pd.get_dummies(X_df)
    Ydummies_df = Y_df

    X = Xdummies_df.values
    Y = Ydummies_df.values

    return X,Y

def calc_hit_tax(X,Y):

    hit_base = max(Counter(Y).itervalues())
    hit_of_tax_base =  100.0 * hit_base / len(Y)
    print( "Taxa de acertos base: %f" % hit_of_tax_base )

    # perc/100
    fit_size_percent = 0.9
    fit_size = fit_size_percent * len(Y)
    fit_data = X[:int(fit_size)]
    fit_making = Y[:int(fit_size)]

    test_size = len(Y) - fit_size
    test_data = X[- int(test_size):]
    test_making = Y[- int(test_size):]

    return fit_data,fit_making,test_data,test_making


def fit_and_predict(model,fit_data,fit_making,test_data,test_making,name):

    model.fit(fit_data,fit_making)
    result = model.predict(test_data)
    hits = test_making == result

    #Acertos
    elements_amount = len(test_data)
    hits_amount = sum(hits)
    hits_percent = 100.0*hits_amount/elements_amount

    print 'Acertos/Total:{0} /{1}  {2}'.format(hits_amount, elements_amount,name)
    print 'Acertos em %:',hits_percent



def run_teste():
    
    fields = ['home','search','login']
    pathFile = 'search.csv'
    varWhatFind = 'bought'

    X,Y = load_data(pathFile,fields,varWhatFind)
    fit_data,fit_making,test_data,test_making = calc_hit_tax(X,Y)

    model1 = AdaBoostClassifier()
    fit_and_predict(model1,fit_data,fit_making,test_data,test_making,"AdaBoostClassifier")

    model1 = MultinomialNB()
    fit_and_predict(model1,fit_data,fit_making,test_data,test_making,"MultinomialNB")


run_teste()