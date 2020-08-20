.. mchoice:: asu_cs_dict_q2
   :author: Erdogan Dogdu
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Dictionaries
   :subchapter: Exercises
   :topics: Dictionaries/Exercises
   :from_source: F
   :answer_a: char_dict.set(char,char_dict[char]+1)
   :answer_b: char_dict[char] = char_dict.get(char,0) + 1
   :answer_c: char_dict[char] += 1
   :answer_d: None
   :correct: b
   :random: 
   :pct_on_first: 0.6
   :total_students_attempting: 25
   :num_students_correct: 19.0
   :mean_clicks_to_correct: 1.3684210526

   What is the short cut statement for if-else statement in this code?::
   
      char_dict = {}
      s = "Now is the time."
      for char in s : 
          if char not in char_dict:
              char_dict[char] = 1 
          else:
              char_dict[char] += 1 
      x = len(char_dict)