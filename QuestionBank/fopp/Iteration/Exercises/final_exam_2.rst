.. activecode:: final_exam_2
   :author: Irma Ravkic
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.515625
   :total_students_attempting: 64
   :num_students_correct: 40.0
   :mean_clicks_to_correct: 1.225

   
   Now, write a program that will print the length for each string in the list below.
   ~~~~
   my_list = ["","hello","", "goodbye", "wonderful", "hello", "goodbye", "I love Python"]
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual('0\n5\n0\n7\n9\n5\n7\n13\n', self.getOutput(), 'Checking output.')
   
   myTests().main()