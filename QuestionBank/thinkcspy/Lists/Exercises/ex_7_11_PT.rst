.. actex:: ex_7_11_PT
   :author: pranoj thapa
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Lists
   :subchapter: Exercises
   :topics: Lists/Exercises
   :from_source: F
   :practice: T
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   Write a function ``sum_of_squares(xs)`` that computes the sum
   of the squares of the numbers in the list ``xs``.  For example,
   ``sum_of_squares([2, 3, 4])`` should return 4+9+16 which is 29:
   ~~~~
   def sum_of_squares(xs):
       # your code here
   
   ====
   import re
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           editText = self.getEditorText()
           self.assertEqual(1, len(re.findall("\s*return", editText)), "Need exactly one return statement")
           self.assertEqual(sum_of_squares([2,3,4]),29,"Tested sum_of_squares on input [2,3,4]")
           self.assertEqual(sum_of_squares([0,1,-1]),2,"Tested sum_of_squares on input [0,1,-1]")
           self.assertEqual(sum_of_squares([5,12,14]),365,"Tested sum_of_squares on input [5,12,14]")
           self.assertEqual(sum_of_squares([1,1.2,4]),18.44,"Tested sum_of_squares on input [1,1.2,4]")
           self.assertEqual(sum_of_squares([-1,-1.2,-4]),18.44,"Tested sum_of_squares on input [-1,-1.2,-4]")
   
   
   myTests().main()