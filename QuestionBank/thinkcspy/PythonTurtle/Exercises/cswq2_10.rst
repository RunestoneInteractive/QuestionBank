.. mchoice:: cswq2_10
   :author: Lloyd Smith
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: PythonTurtle
   :subchapter: Exercises
   :topics: PythonTurtle/Exercises
   :from_source: F
   :answer_a: 0 'a' 'b' 'c' 1 'a' 'b' 'c' 2 'a' 'b' 'c'
   :answer_b: 1 2 3 a b c
   :answer_c: 1 a 2 b 3 c
   :answer_d: a 1 b 2 c 3
   :correct: a
   :random: 
   :feedback_a: Yes - the inner loop prints its 3 values every time the outer loop prints one of its values
   :feedback_b: No - the inner loop prints its 3 values every time the outer loop prints one of its values
   :feedback_c: No - the inner loop prints its 3 values every time the outer loop prints one of its values
   :feedback_d: No - the inner loop prints its 3 values after the outer loop prints one of its values
   :pct_on_first: 0.5714285714
   :total_students_attempting: 105
   :num_students_correct: 105.0
   :mean_clicks_to_correct: 1.8761904762

   10. What does the following code print?::
   
      for i in range(3):
          print(i, end = ' ')
          for character in ['a', 'b', 'c']:
              print(character, end = ' ')