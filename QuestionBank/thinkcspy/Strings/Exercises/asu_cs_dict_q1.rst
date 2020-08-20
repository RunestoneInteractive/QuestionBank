.. parsonsprob:: asu_cs_dict_q1
   :author: Erdogan Dogdu
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: Exercises
   :topics: Strings/Exercises
   :from_source: F
   :pct_on_first: 0.6666666667
   :total_students_attempting: 12
   :num_students_correct: 12.0
   :mean_clicks_to_correct: 3.1666666667

   Put the following statements in order so the function takes a list and returns a dictionary of distinct elements with their occurrence counts in the list.
   -----
   def countlist(lst):
   =====
       d = {}
   =====
       for w in lst:
   =====
           d[w] = d.get(w,0) + 1
   =====
       return d