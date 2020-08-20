.. parsonsprob:: filter_words-Parsons
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPWhileAndForLoops
   :subchapter: Exercises
   :topics: CSPWhileAndForLoops/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.4571428571
   :total_students_attempting: 140
   :num_students_correct: 138.0
   :mean_clicks_to_correct: 2.4492753623

   Finish the function to return a new list with all the words removed that are of 
   length 3 or less.
   -----
   def filter_words(word_list):
   =====
   def filter_words(word_list: #paired
   =====
       new_list = []
   =====
       for word in word_list:
   =====
           if len(word) > 3:
   =====
           if len(word) >= 3: #paired
   =====
               new_list.append(word)
   =====
               new_list += word #paired
   =====
       return new_list
   =====
       return newList #paired