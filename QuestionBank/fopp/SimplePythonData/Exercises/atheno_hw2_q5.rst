.. actex:: atheno_hw2_q5
   :author: Atheno Chen
   :difficulty: 1.2896028559
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :autograde: unittest
   :pct_on_first: 0.027027027
   :total_students_attempting: 37
   :num_students_correct: 12.0
   :mean_clicks_to_correct: 5.9166666667

   Write a program to accept an integer ``num`` as the input and output a boolean value to determine whether it is an odd number or not.
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def test_radius(self):
           self.assertIn("num", self.getEditorText(), 'num variable')
           self.assertIn(str(num % 2 != 0)[:4], self.getOutput(), 'Checking answer.')
   myTests().main()