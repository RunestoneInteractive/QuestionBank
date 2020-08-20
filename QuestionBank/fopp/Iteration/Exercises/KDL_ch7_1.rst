.. activecode:: KDL_ch7_1
   :author: Kaelyn Leake
   :difficulty: 1.2492019359
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.1538461538
   :total_students_attempting: 13
   :num_students_correct: 13.0
   :mean_clicks_to_correct: 5.2307692308

   
   
   Cobalt-60, a radioactive form of cobalt used in cancer therapy, decays over a period of time. Each year, 12% of the amount present at the beginning of the year will have decayed. If a container of cobalt-60 initially contains 10 grams, determine the ``amount_remaining`` after five years. Use a for loop to solve, print the amount remaining after calculating.
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
   
           self.assertEqual(amount_remaining,10*.88**5,feedback="Correct amount remaining")
           self.assertIn('for ', self.getEditorText(), 'Contains for loop')
           self.assertTrue(re.search(str(5.2)[:2], self.getOutput()), 'Checking sentence.')
   myTests().main()