.. mchoice:: more_db_2
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameStrings
   :subchapter: Exercises
   :topics: CSPNameStrings/Exercises
   :from_source: F
   :correct: d
   :answer_a: Logical: id, Primary: name, Foreign: from_id
   :answer_b: Logical: from_id, Primary: id, Foreign: name
   :answer_c: Logical: name, Primary: from_id, Foreign: id
   :answer_d: Logical: name, Primary: id, Foreign: from_id
   :feedback_a: id is a primary key
   :feedback_b: from_id is a foreign key
   :feedback_c: the primary key is the foreign key
   :feedback_d: name is a logical key, id is a primary key, and from_id is a foreign key
   :pct_on_first: 0.4049586777
   :total_students_attempting: 121
   :num_students_correct: 121.0
   :mean_clicks_to_correct: 2.041322314

   Which of the following is correct?
   
   :: 
   
       cur.execute('''CREATE TABLE IF NOT EXISTS People
          (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)''')
       cur.execute('''CREATE TABLE IF NOT EXISTS Follows
          (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')