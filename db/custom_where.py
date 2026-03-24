import sqlite3

def customRead(w):
    '''use SQL WHERE with wildcards to retrieve matching values'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st = f'''
    SELECT creature, count, cost
    FROM zoo
    WHERE creature = '{w}'
'''
    try:
        curs.execute(st)
        conn.commit()
        rows = curs.fetchall()
        return rows
    except Exception as err:
        print(err)


    conn.close() # rememer to tidy up


if __name__ == '__main__':
    w = input('Which creature: ')
    results = customRead(w)
    print(results) # we have a list