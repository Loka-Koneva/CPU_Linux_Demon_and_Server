import sqlite3

db = sqlite3.connect('db_1.sqlite3')
sql = db.cursor()
list = []
for i in sql.execute('SELECT * FROM record'):
    #print(i[0])
    list.append(i[0]+'%')

list_in_line = '  '.join(list)
list_last = list[::-1]
list_last_in_line = '  '.join(list_last)
print(list_in_line)
print(list_last_in_line)
