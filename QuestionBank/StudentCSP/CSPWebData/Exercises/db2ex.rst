.. parsonsprob:: db2ex
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPWebData
   :subchapter: Exercises
   :topics: CSPWebData/Exercises
   :from_source: F
   :adaptive:
   :numbered: left

   Put the blocks below in order to connect to a database, create a cursor, use the cursor to insert into a table, select data from the table and print it.
   -----
   import sqlite3
   ===== 
   conn = sqlite3.connect('/Users/barbarer/Desktop/music.sqlite')
   =====
   cur = conn.cursor()
   =====
   cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
    ('Thunderstruck', 20))
   cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
    ('My Way', 15))
   =====
   conn.commit()
   =====
   print('Tracks:')
   cur.execute('SELECT title, plays FROM Tracks')
   =====
   for row in cur:
   =====
       print(row)
   =====
   cur.close()