.. mchoice:: cswq6_9
   :author: Lloyd Smith
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Dictionaries
   :subchapter: Exercises
   :topics: Dictionaries/Exercises
   :from_source: F
   :answer_a: 11
   :answer_b: 16
   :answer_c: 15
   :answer_d: 12
   :correct: a
   :random: 
   :pct_on_first: 0.4642857143
   :total_students_attempting: 112
   :num_students_correct: 107.0
   :mean_clicks_to_correct: 1.9906542056

   9. What is the value of x after executing the following code?::
   
      char_dict = {}
      s = "Now is the time."
      for char in s : 
          if char not in char_dict:
              char_dict[char] = 1 
          else:
              char_dict[char] += 1 
      x = len(char_dict)