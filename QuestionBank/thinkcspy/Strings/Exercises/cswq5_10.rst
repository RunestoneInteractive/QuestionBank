.. parsonsprob:: cswq5_10
   :author: Lloyd Smith
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: Exercises
   :topics: Strings/Exercises
   :from_source: F
   :pct_on_first: 0.8129032258
   :total_students_attempting: 155
   :num_students_correct: 153.0
   :mean_clicks_to_correct: 1.8496732026

   10. Put the following statements in the correct order to define a function that returns the number of vowels in string s.
   -----
   def count_vowels(s):
   '''Returns the number of vowels in string s'''
   =====
       num_vowels = 0
   =====
       for char in s:
   =====
           if char in "aeiou":
   =====
            num_vowels = num_vowels + 1
   =====
       return num_vowels
   =====