.. mchoice:: cswq2_9
   :author: Lloyd Smith
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: PythonTurtle
   :subchapter: Exercises
   :topics: PythonTurtle/Exercises
   :from_source: F
   :answer_a: prints the average of the numbers in the list
   :answer_b: prints the numbers in the list
   :answer_c: prints the first and last number in the list
   :answer_d: it's impossible to tell what this code does without running it
   :correct: a
   :random: 
   :feedback_a: Yes, this is a common pattern - averaging a list of numbers
   :feedback_b: No, notice that total holds the sum of the numbers in the list and it's divided by the number of items in the list
   :feedback_c: No, notice that total holds the sum of the numbers in the list and it's divided by the number of items in the list
   :feedback_d: Notice that total holds the sum of the numbers in the list and it's divided by the number of items in the list - you should be able to figure out what the result is
   :pct_on_first: 0.8780487805
   :total_students_attempting: 123
   :num_students_correct: 121.0
   :mean_clicks_to_correct: 1.1900826446

   9. What does the following code do?::
   
      total = 0
      for num in [27, 12, 45, 100, 12]:
          total = total + num
      print(total / 5)