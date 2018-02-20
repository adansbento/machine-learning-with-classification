import csv


def load_access():

    datas = []
    making = []

    file = open('page_access.csv', 'rb')
    reader = csv.reader(file)
    reader.next()

    for home,how_work,contact, bought in reader:
        datas.append([ int(home),int(how_work), int(contact) ])
        making.append( int(bought))

    return datas,making

