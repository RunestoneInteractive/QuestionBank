.. parsonsprob:: pp_2_hours2seconds_jcomes
   :author: Jonny Comes
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :noindent: 
   :pct_on_first: 0.6666666667
   :total_students_attempting: 3
   :num_students_correct: 3.0
   :mean_clicks_to_correct: 2.0

   Write a program that will convert hours to seconds. This program will also need to get input from a user to see how many hours should be converted and the result should be printed to the user.
   -----
   user_hours = input("How many hours should be converted?: ")
   =====
   num_hours = int(user_hours)
   =====
   minutes = num_hours * 60
   =====
   seconds = minutes * 60
   =====
   print("Number of seconds: " + str(seconds))