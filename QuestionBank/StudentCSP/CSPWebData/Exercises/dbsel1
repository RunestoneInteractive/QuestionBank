.. parsonsprob:: dbsel1
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPWebData
   :subchapter: Exercises
   :topics: CSPWebData/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.3035714286
   :total_students_attempting: 168
   :num_students_correct: 166.0
   :mean_clicks_to_correct: 3.8253012048

   Put the code blocks in order to read data from a database, calculate the number of rows read, print each row.  Then it should print the number of rows and close the cursor.
   -----
   import sqlite3
   =====
   conn = sqlite3.connect('spider.sqlite')
   =====
   cur = conn.cursor()
   =====
   cur = cursor() #distractor
   =====
   cur.execute('SELECT * FROM Twitter')
   =====
   conn.execute('SELECT * FROM Twitter') #distractor
   =====
   count = 0
   for row in cur:
   =====
       print(row)
       count = count + 1
   =====
   print(count, 'rows.')
   conn.close()