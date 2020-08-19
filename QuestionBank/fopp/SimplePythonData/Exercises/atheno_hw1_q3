.. actex:: atheno_hw1_q3
   :author: Atheno Chen
   :difficulty: 4.0
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :autograde: unittest
   :pct_on_first: 0.0
   :total_students_attempting: 3
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 7.0

   Write a program that will compute the perimeter of a right trapezoid. Prompt the user to enter the base 1, base 2 and height and save them to variables called ``a``, ``b`` and ``h``. Print a nice message back to the user with the answer.
   ~~~~
   import math
   
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def test_radius(self):
           self.assertIn("a", self.getEditorText(), 'base 1 variable')
           self.assertIn("b", self.getEditorText(), 'base 2 variable')
           self.assertIn("h", self.getEditorText(), 'height variable')
           self.assertIn(str(math.sqrt((b-a)**2 + h**2) + a + b + h)[:4], self.getOutput(), 'Checking answer.')
   myTests().main()