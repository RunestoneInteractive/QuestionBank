.. activecode:: sks_cw2_ex2
   :author: Shishir Shah
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F

   [25 pts] Consider the below program:

   a) What seems to be the purpose of the above program? Describe the same as comment at start of the program.

   b) Can you discover any errors? List any errors you discover. State if they are a syntax, runtime, or logic error, and indicate erroneous lines by comments above them.  Correct the erroneous lines.

   c)	Run the program and state as a comment the result for input scores: quiz 1 = 100, quiz2 = 60,  mid_term= 90, final = 70. 

   d) In the program, all quizzes and exams were scored out of a 100. Suppose, the quizzes are scored out of 50 each, and mid term and final are still scored out of 100. However, the total weight of quizzes should still be 30%, mid term 30%, and final 40%. How will you modify the program to reflect this change?  Show this change using a new variable ``weighted_total`` and print the value resulting from this new calculation.
   ~~~~
   quiz1 = int(input('Enter Quiz 1 grade: '))
   quiz2 = int(input('Enter Quiz 2 grade: '))
   midterm = int(input('Enter Midterm grade: '))
   final = int(input('Enter Final grade: '))

   quiz_average = quiz1 + quiz2 / 2

   total = quiz_average*0.3 + mid_term*0.3 + final*0.4

   print('Your class grade is:', “total”)