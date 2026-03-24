import sqlite3

def retrieve():
    '''retrieve from the db table'''
    # make a connection
    conn = sqlite3.connect('my_db')
    # get a cursor
    curs = conn.cursor()
    # write an SQL statement
    st = 'SELECT creature, count, cost FROM zoo'
    # execute and commit the SQL    
    try:
        curs.execute(st)
        conn.commit()
        # return the retrieved values
        rows = curs.fetchall() # retrieves zero or more, up to all the rows in the table
        return rows

    except Exception as err:
        print(err)

if __name__ == '__main__':
    a = retrieve()
    print(a)