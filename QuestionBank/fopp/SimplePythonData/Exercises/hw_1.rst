.. actex:: hw_1
   :author: Atheno Chen
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :autograde: unittest

   Ask the user for the temperature in Fahrenheit and store it in a variable call ``deg_f``. Calculate the equivalent temperature in degrees Celsius and store it in ``deg_c``. Output a message to the user giving the temperature in Celsius.
   ~~~~

   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertIn('deg_f', self.getEditorText())
           self.assertIn('deg_c', self.getEditorText())
           ans = (deg_f - 32)*5/9
           self.assertAlmostEqual(ans, deg_c)
           self.assertIn(str(ans)[:min(len(str(ans)), 5)],    self.getOutput(), 'Checking answer.')
   myTests().main()