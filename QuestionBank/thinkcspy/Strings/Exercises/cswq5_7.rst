.. mchoice:: cswq5_7
   :author: Lloyd Smith
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: Exercises
   :topics: Strings/Exercises
   :from_source: F
   :answer_a: t h e&nbsp;&nbsp;&nbsp;q u i c k&nbsp;&nbsp;&nbsp;b r o n&nbsp;&nbsp;&nbsp;f o x
   :answer_b: t h e&nbsp;&nbsp;&nbsp;q u i c k&nbsp;&nbsp;&nbsp;b r o
   :answer_c: w
   :answer_d: t h e&nbsp;&nbsp;&nbsp;q u i c k&nbsp;&nbsp;&nbsp;b r o w n&nbsp;&nbsp;&nbsp;f o x
   :correct: a
   :random: 
   :pct_on_first: 0.2641509434
   :total_students_attempting: 106
   :num_students_correct: 105.0
   :mean_clicks_to_correct: 2.1619047619

   7. What does the following code print?::
   
      s = "the quick brown fox"
      for char in s:
          if char == 'w':
              continue
          print(char, end = ' ')