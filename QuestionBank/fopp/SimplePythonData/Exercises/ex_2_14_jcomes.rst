.. actex:: ex_2_14_jcomes
   :author: Jonny Comes
   :difficulty: 1.1472556894
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :autograde: unittest
   :pct_on_first: 0.1428571429
   :total_students_attempting: 7
   :num_students_correct: 4.0
   :mean_clicks_to_correct: 3.5

   Ask the user for the temperature in Fahrenheit and store it in a variable call ``deg_f``. Calculate the equivalent temperature in degrees Celsius and store it in ``deg_c``. Output a message to the user giving the temperature in Celsius.
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertIn('input', self.getEditorText(), 'Check that input is used.')
           self.assertIn('deg_f', self.getEditorText(), 'Check deg_f is used.')
           self.assertIn('deg_c', self.getEditorText(), 'Check deg_c is used.')
           ans = (deg_f - 32)*5/9
           self.assertAlmostEqual(ans, deg_c, 7, 'Check value in deg_c.')
           self.assertIn(str(ans)[:min(len(str(ans)), 5)],    self.getOutput(), 'Checking answer.')
   myTests().main()