.. activecode:: final_exam_1
   :author: Irma Ravkic
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.4590163934
   :total_students_attempting: 61
   :num_students_correct: 36.0
   :mean_clicks_to_correct: 1.6111111111

   
   Consider the list given below. Write the program that uses a for loop will to print each item of the list on the separate line.
   ~~~~
   my_list = ["","hello","", "goodbye", "wonderful", "hello", "goodbye", "I love Python"]
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual('\nhello\n\ngoodbye\nwonderful\nhello\ngoodbye\nI love Python\n', self.getOutput(), 'Checking output.')
   
   myTests().main()