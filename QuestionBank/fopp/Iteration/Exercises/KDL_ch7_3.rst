.. activecode:: KDL_ch7_3
   :author: Kaelyn Leake
   :difficulty: 1.1902996602
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.2307692308
   :total_students_attempting: 13
   :num_students_correct: 13.0
   :mean_clicks_to_correct: 4.2307692308

   In mathematics, the notation n! represents the factorial of the nonnegative integer n. The factorial of n is the product of all the nonnegative integers from 1 to n. For example,
   4!=1*2*3*4=24 and 7!=1*2*3*4*5*6*7=5040.
   Write a program that lets the user enter a nonnegative ``integer_value`` then uses a for loop to calculate the ``factorial`` of that number. Display the factorial.
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           fact=1
           for n in range(1,int(integer_value)+1):
              fact*=n
           self.assertEqual(factorial,fact,feedback="Correct factorial value")
           self.assertIn('for ', self.getEditorText(), 'Contains for loop')
           self.assertTrue(re.search(str(fact)[:1], self.getOutput()), 'Checking sentence.')
   myTests().main()