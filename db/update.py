import sqlite3

def updateOneItem(w):
    '''implement changes to one row in the db'''
    count=(int(float(w['count'])))
    creature = str(w['creature'])
    conn = sqlite3.connect()
    curs = conn.cursor()
    # NB within SQL we use quotes for string-like values but NOT for numeric values
    st = f'''
    UPDATE zoo
    SET count={count}
    WHERE creature = '{creature}' 
'''

if __name__ == '__main__':
    whichItem = input('Which creature: ')
    w = {'creature':whichItem, 'count':3} # hard-code a new value for count
    updateOneItem(w)