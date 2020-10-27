from django.shortcuts import render
import sqlite3

def recieve_of_data(request):
    db = sqlite3.connect('db_1.sqlite3')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS record(record_of_cpu TEXT)""")
    db.commit()
    cpu = request.GET.get('cpu_data')
    sql.execute(f"INSERT INTO record VALUES('{cpu}')")
    db.commit()
    return render (request, 'recieve_data.html')

def show_of_data(request):
    db = sqlite3.connect('db_1.sqlite3')
    sql = db.cursor()
    list_with_cpu_data = []
    for i in sql.execute('SELECT * FROM record'):
        list_with_cpu_data.append(i[0]+'%')
    list_with_cpu_data_last = list_with_cpu_data[::-1]
    return render(request, 'show_of_data.html', {'list_with_cpu_data': list_with_cpu_data_last})
