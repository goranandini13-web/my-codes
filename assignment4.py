#question1---
import csv
#dummy data
data=[
    ["nandini","jaipur","7367397729","nandini@gmail.com"],
    ["rihana","ajmer","378765689","rihana@gamail.com"],
    ["nia","udaipur","36738677","nia@gamil.com"]
]
#create a csv file-
with open("address_book.csv","w",newline='')as file:
    writer=csv.writer(file)
    #column name--
    writer.writerow(["Name","address","mobile","email"])
    #insert data--
    writer.writerows(data)
    print("csv file is created succesfully!")
    

    #question2--
    import sqlite3

    #creaate database
    conn= sqlite3.connect("college.db")
    cursor = conn.cursor()

    #create tables--
    cursor.execute('''
    CREATE TABLE learners(
                   id INTEGER PRIMARY KEY,name TEXT,
                   course TEXT
                   )
                   ''') 
    
    cursor.execute('''
                   CREATE TABLE teacher(
                   id INTEGER PRIMARY KEY,
                   name TEXT,
                   subject TEXT)
                   ''')
    #insert record---
    cursor.execute("INSERT INTO learners VALUES(1,'nandini','b.tech')")
    cursor.execute("INSERT INTO learners VALUES(2,'rahul','bca')")

    cursor.execute("INSERT INTO teacher VALUES(1,'sharma','python')")
    cursor.execute("INSERT INTO teacher VALUES(2,'rajput','dbms')")

    #select oprerations--
    print("students:")
    for row in cursor.execute("SELECT*FROM learners"):
        print(row)

        #update data--
        cursor.execute("UPDATE learners SET course ='MCA' WHERE id=2")

        #delete data--
        cursor.execute("DELETE FROM teacher WHERE ID=2")

        conn.commit()
        conn.close()

        print("database operation is completed")


    
    

