.. parsonsprob:: mt1dict1
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPIntroData
   :subchapter: Exercises
   :topics: CSPIntroData/Exercises
   :from_source: F
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.456445993
   :total_students_attempting: 287
   :num_students_correct: 285.0
   :mean_clicks_to_correct: 2.5192982456

   Put the blocks in order to define the function greater_dictionary. 
   It takes a dictionary d and an integer cutoff and returns a dictionary 
   that contains only the key-value pairs where the key is greater than 
   or equal to the cutoff.
   -----
   def greater_dictionary(d, cutoff):
   =====
   def greater_dictionary(self, d, cutoff): #paired
   =====
       result = {}
   =====
       for key in d.keys():
   =====
       for key in range(d): #paired
   =====
           if key >= cutoff:
   =====
           if key > cutoff: #paired
   =====
               result[key] = d[key]
   =====
               d[key] = result[key] #paired
   =====
       return result