.. parsonsprob:: dbCreate_PP
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 15-database
    :subchapter: 15-creatingDBtable
    :topics: 15-database/15-creatingDBtable
    :from_source: T
    :practice: T

    Put the following code in order to create a cursor, make a table called "Cats" with
    two text columns ("Name" and "Breed"). Then add the rows for Whiskers, Ruby, and Milo in
    the table and print all the rows before exiting the table.
    -----
    import sqlite3

    conn = sqlite3.connect('pets.sqlite')
    cur = conn.cursor()
    =====
    cur.execute('DROP TABLE IF EXISTS Cats')
    cur.execute('CREATE TABLE Tracks (name TEXT, breed INTEGER)')
    =====
    cur.execute('INSERT INTO Cats (name, breed) VALUES (?, ?)',
        ('Whiskers', 'Ragdoll'))
    cur.execute('INSERT INTO Cats (name, breed) VALUES (?, ?)',
        ('Ruby', 'Persian'))
    cur.execute('INSERT INTO Cats (name, breed) VALUES (?, ?)',
        ('Milo', 'Russian Blue'))
    =====
    conn.commit()
    =====
    print('Cats:')
    cur.execute('SELECT name, breed FROM Cats')
    =====
    for row in cur:
         print(row)
    =====
    cur.close()