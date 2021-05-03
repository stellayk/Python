import pymysql

config = {
    'host':'localhost',
    'user':'stella',
    'password':'star',
    'database':'work',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True}

import sqlite3

try:
    conn=sqlite3.connect("../examples/sqlite_db")
    cursor=conn.cursor()

    sql="""create table if not exists good(
    code integer primary key,
    name text(30) unique not null,
    su integer default 0,
    dan real default 0.0
    )"""
    cursor.execute(sql)

    '''
    cursor.execute("insert into goods values(1, 'fridge', 2, 8500000)")
    cursor.execute("insert into goods values(2, 'washer', 3, 5500000)")
    cursor.execute("insert into goods (code, name) values(3, 'microwave')")
    cursor.execute("insert into goods (code, name, dan) values(4, 'HDTV', 15000000)")
    conn.commit()
    '''

    code=int(input('code: '))
    name=input('name: ')
    su=int(input('su: '))
    dan=int(input('dan: '))

    sql=f"insert into goods values({code}, '{name}', {su}, {dan})"
    cursor.execute(sql)
    conn.commit()

    '''
    code = int(input('new code:' ))
    su = int(input('new su:' ))
    dan = int(input('new dan:' ))
    
    sql = f"update goods set su={su}, dan={dan} where code={code}"
    cursor.execute(sql)
    conn.commit()
    '''

    '''
    code = int(input('delete code: '))
    sql = f"delete from goods where code={code}"
    cursor.execute(sql)
    conn.commit()
    '''

    sql = "select*from goods"
    cursor.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        print(row[0],row[1],row[2],row[3])

    print('length of rows: ', len(rows))

    name = input("name: ")
    sql = f"select*from goods where name like '%{name}%'"
    cursor.execute(sql)
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print('no record')

except Exception as e:
    print('db error: ', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()