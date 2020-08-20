.. parsonsprob:: db2exv2
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPWebData
   :subchapter: Exercises
   :topics: CSPWebData/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.0068965517
   :total_students_attempting: 145
   :num_students_correct: 144.0
   :mean_clicks_to_correct: 7.7916666667

   Put the blocks below in order to connect to a database, create a cursor, use the cursor to insert into a table, commit the change, select data from the table and print it.  Then close the cursor..
   -----
   import sqlite3
   ===== 
   conn = sqlite3.connect('music.sqlite')
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
   cur.execute('SELECT title, plays FROM Tracks')
   =====
   cur.execute('SELECT title and plays FROM Tracks') #distractor
   =====
   for row in cur:
   =====
       print(row)
   =====
   cur.close()