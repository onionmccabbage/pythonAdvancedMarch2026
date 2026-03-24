import sqlite3

def createTable():
    '''create or open a database and then make a table inside it'''
    # we need a connection to a db (I/O bound)
    conn = sqlite3.connect('my_db') # if it doesn't exist, create it, if it already exists, connect to it
    # we make a cursor to operate within the db
    curs = conn.cursor()
    # we need an SQL statement
    st = 'CREATE TABLE IF NOT EXISTS zoo (creature VARCHAR(32) PRIMARY KEY, count int, cost float )'
    # implement the SQL on the db
    try:
        curs.execute(st) # at this point no changes happen to the db
        conn.commit()    # here any db changes will be persisted
        conn.close()     # tidy up
    except Exception as err:
        print(err)

if __name__ == '__main__':
    '''exercise this module'''
    createTable() # this will make sure our empty table exists in the db