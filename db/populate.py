import sqlite3

def populate(creature_tuple):
    '''iterate over the tuple to populate into the db table'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # we often use tripple quotes for SQL statements since it allows new lines within the quotes
    st = '''
    INSERT INTO zoo
    VALUES (?, ?, ?)
''' # NB we use ? to allow injection of values, which lets us validate
    # here we iterate over the collection, inecting each dict of values to replace the ?
    for item in creature_tuple:
        try:
            if type(item['creature'])==str and item['creature'] !='':
                n = item['creature']
            else:
                raise TypeError('Creature name must be a non empty string')
            if type(item['count'] == int) and item['count'] >= 0:
                count = item['count']
            else:
                raise TypeError('Creature count must be integer zero or more')
            if type(item['cost'] == float) and item['cost'] >= 0:
                cost = item['cost']
            else:
                raise TypeError('Creature cost must be float zero or more')
            # here are the lines I missed before lunch!
            curs.execute(st, (n, cost, count))
            conn.commit()

        except Exception as err:
            print(err)
    conn.close()

if __name__ == '__main__':
    creature_tuple = ( # normally this data would come from an API, a file, a microservcie etc.
        {'creature':'Albatros', 'count':1,   'cost':120.99},
        {'creature':'Bear',     'count':5,   'cost':120.99},
        {'creature':'Carp',     'count':120, 'cost':120.99},
        {'creature':'Deer',     'count':32,  'cost':120.99},
        {'creature':'Elk',      'count':7,   'cost':120.99},
    )
    populate(creature_tuple)