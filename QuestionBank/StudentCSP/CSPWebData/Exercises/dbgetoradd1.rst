.. parsonsprob:: dbgetoradd1
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPWebData
   :subchapter: Exercises
   :topics: CSPWebData/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.0
   :total_students_attempting: 27
   :num_students_correct: 18.0
   :mean_clicks_to_correct: 18.3333333333

   Put the blocks in order to get the id from the database for acct if it exists and if not add it to the People table and get the id from adding it. 
   -----
   # See if the screen name (acct) is in the database
    cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',
               (acct, ))
   =====
    try:
   =====
        # it is so get the key (id)
        id = cur.fetchone()[0]
   =====
    except:
   =====
        # not there so add it
        cur.execute('''INSERT OR IGNORE INTO People
                    (name, retrieved) VALUES (?, 0)''', (acct, ))
   =====
        conn.commit()
   =====
        if cur.rowcount != 1:
   =====
            print('Error inserting account:', acct)
            continue
   =====
        id = cur.lastrowid