import sqlite3

def writeData():
    '''commit one creature to the database table'''
    # make a connection
    conn = sqlite3.connect('my_db')
    # get a cursor
    curs = conn.cursor()
    # write an SQL statement
    st = 'INSERT INTO zoo VALUES ("Penguin", 16, 0.52)'
    # execute and commit the SQL    
    try:
        curs.execute(st)
        conn.commit()
    except Exception as err:
        print(err)

if __name__ == '__main__':
    writeData()