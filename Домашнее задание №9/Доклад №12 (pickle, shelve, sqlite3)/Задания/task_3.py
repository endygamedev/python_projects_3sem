"""
    Создайте таблицу employees и заполните ее данными, как на картинке.
    Повысьте зарплату на 1000 долларов всем работикам младше 30 лет и удалите из таблицы работников старше 40
"""


import sqlite3


conn = sqlite3.connect("db_employees.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE employees (name text, salary$ integer, age integer)")

employees = [('John Doe', 5000, 35),
             ('Marie Paige', 6000, 25),
             ('Megan Flores', 3000, 29),
             ('Harmony Simmons', 4000, 42)]

cursor.executemany("INSERT INTO employees VALUES (?, ?, ?)", employees)
conn.commit()

sql_query1 = "UPDATE employees SET salary$ = salary$ + 1000 WHERE age < 30"
cursor.execute(sql_query1)
conn.commit()

sql_query2 = "DELETE FROM employees WHERE age > 40"
cursor.execute(sql_query2)
conn.commit()