.. parsonsprob:: pp_2_17_fixed_typos
   :author: Jonny Comes
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :noindent: 
   :pct_on_first: 0.75
   :total_students_attempting: 8
   :num_students_correct: 8.0
   :mean_clicks_to_correct: 1.375

   Write a program that will convert tablespoons to teaspoons. This program will also need to get input from a user to see how many tablespoons should be converted and the result should be printed to the user.
   -----
   user_tablespoons = float(input("How many tablespoons should be converted?: "))
   =====
   teaspoons = user_tablespoons * 3
   =====
   print("Number of teaspoons: " + str(teaspoons))