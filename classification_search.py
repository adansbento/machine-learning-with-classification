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

def create_hit_base(Y):
    hit_base = max(Counter(Y).itervalues())
    hit_of_tax_base =  100.0 * hit_base / len(Y)
    print( "Taxa de acertos base (chuta sempre o elemento de maior frequencia): %f" % hit_of_tax_base )


def calc_hit_tax(X,Y):

    # 80 % treino 10% teste 10% validacao
    fit_size_percent = 0.8
    test_size_percent = 0.1
    validation_size_percent = 0.1

    fit_size = fit_size_percent * len(Y)
    fit_data = X[0:int(fit_size)]
    fit_making = Y[0:int(fit_size)]
    fit_end = len(fit_data)

    test_size = test_size_percent * len(Y)
    test_end = fit_end + test_size
    test_data = X[int(fit_end):int(test_end)]
    test_making = Y[int(fit_end):int(test_end)]

    validation_size = validation_size_percent * len(Y)
    validation_end =  test_end + validation_size
    validation_data = X[ int(test_end):int(validation_end)]
    validation_making = Y[int(test_end):int(validation_end)]
    
    return fit_data,fit_making,test_data,test_making,validation_data,validation_making

def fit_and_predict(model,data,making,fit_data,fit_making,name):

    #treinar
    model.fit(fit_data,fit_making)

    #prever
    result = model.predict(data)
    hits = making == result

    #Acertos
    elements_amount = len(data)
    hits_amount = sum(hits)
    hits_percent = 100.0*hits_amount/elements_amount

    print 'Acertos/Total {0}: {1}/{2}'.format(name,hits_amount, elements_amount)
    print 'Acertos em %:',hits_percent

    return hits_amount

def run_test():
    
    fields = ['home','search','login']
    pathFile = 'search.csv'
    varWhatFind = 'bought'

    X,Y = load_data(pathFile,fields,varWhatFind)
    fit_data,fit_making,test_data,test_making,validation_data,validation_making = calc_hit_tax(X,Y)

    # cria um algortimo que chuta sempre o elemeto de maior frequencia
    create_hit_base(validation_making)

    adaBoostModel = AdaBoostClassifier()
    hitAdaBoost = fit_and_predict(adaBoostModel,test_data, test_making,fit_data,fit_making," AdaBoostClassifier ")

    multinomialModel = MultinomialNB()
    hitMultinomial  = fit_and_predict(multinomialModel,test_data, test_making,fit_data,fit_making," MultinomialNB ")

    #Seleciona o algoritmo com melhor resultado
    betterModel = multinomialModel
    
    if hitAdaBoost > hitMultinomial:
        betterModel = adaBoostModel
        
    fit_and_predict(betterModel,validation_data, validation_making,fit_data,fit_making," O melhor entre todos com dados reais")
    
run_test()