.. parsonsprob:: cswq5_8
   :author: Lloyd Smith
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: Exercises
   :topics: Strings/Exercises
   :from_source: F
   :pct_on_first: 0.3125
   :total_students_attempting: 160
   :num_students_correct: 154.0
   :mean_clicks_to_correct: 5.3376623377

   8. Put the following statements in the correct order to define a function that returns a string with all the vowels removed.
   -----
   def remove_vowels(s) :
   '''Returns string s with all vowels removed'''
   =====
       new_string = ""
   =====
       for char in s:
   =====
          if char not in "aeiou":
   =====
              new_string = new_string + char
   =====
       return new_string