from database import cursor, db

#add entry
def add_log(text, user):
    sql = ("INSERT INTO logs(text, user) VALUES (%s, %s)")
    cursor.execute(sql, (text, user,))
    db.commit()
    log_id = cursor.lastrowid
    print("Added log {}".format(log_id))
#entries added
# add_log('This is log one', 'bob')
# add_log('This is log two', 'bruce')
# add_log('This is log three', 'c')

#get all from logs
# def get_logs():
#     sql = ("SELECT * FROM logs ORDER BY created DESC")
#     cursor.execute(sql)
#     result = cursor.fetchall()

#     for row in result:
#         print(row)
# get_logs()

#single query
def get_log(id):
    sql = ("SELECT * FROM logs WHERE id=%s")
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    
    for row in result:
        print(row)
#get_log(2)

#update entry
def update_log(id, text):
    sql = ("UPDATE logs SET text = %s WHERE id = %s")
    cursor.execute(sql, (text, id,))
    db.commit()
    print("Log updated")
#update_log(2, 'Updated log')
#get_log(2)

#delete entry
def delete_log(id):
    sql = ("DELETE FROM logs WHERE id = %s")
    cursor.execute(sql, (id,))
    db.commit()
    print("Log removed")
delete_log(2)




