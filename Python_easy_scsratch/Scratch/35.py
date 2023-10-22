import pymysql

connection = pymysql.connect(user='root', password='mysql', host='localhost', database='pythontut')
c = connection.cursor()


#c.execute("CREATE SCHEMA pythontut")
#c.execute("CREATE TABLE employee(id INT NOT NULL, name VARCHAR(20),PRIMARY KEY(id))")

#c.execute("INSERT INTO employee VALUES(1, 'raunak'),(2, 'mritunjay'),(3, 'vasant')")
#connection.commit()

def ret():
    c.execute("SELECT * FROM employee")
    #print(c.fetchall())
    for row in c.fetchall():
        print(row)



def up():
    c.execute("UPDATE employee SET name='Canan' WHERE id=3")
    connection.commit()



def delete():
    c.execute("DELETE FROM employee WHERE name='mritunjay'")
    connection.commit()

def drop():
    c.execute("DROP TABLE employee")
    connection.commit()

def schema():
    c.execute("DROP SCHEMA pythontut")
    connection.commit()



schema()

#drop()
#delete()
#up()

#ret()
c.close()
connection.close()
