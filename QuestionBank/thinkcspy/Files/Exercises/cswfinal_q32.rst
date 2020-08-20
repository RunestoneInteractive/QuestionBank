.. mchoice:: cswfinal_q32
   :author: Lloyd Smith
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Files
   :subchapter: Exercises
   :topics: Files/Exercises
   :from_source: F
   :answer_a: prints all the files in the program's folder
   :answer_b: prints a list of all the states in alphabetical order
   :answer_c: prints all the words in the original (1900) edition of The Wizard of Oz
   :answer_d: prints nothing
   :correct: a
   :random: 
   :pct_on_first: 0.4907407407
   :total_students_attempting: 108
   :num_students_correct: 107.0
   :mean_clicks_to_correct: 1.8504672897

   32. What does the following function print? (You should run it to see.)::
   
      import os
      def check():
          something = os.listdir(".")
          for x in something:
              print(x)