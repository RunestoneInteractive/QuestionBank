.. activecode:: KDL_ch2_1
   :author: Kaelyn Leake
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.0714285714
   :total_students_attempting: 14
   :num_students_correct: 14.0
   :mean_clicks_to_correct: 4.5714285714

   Calculate the ``area`` of a hexagon. Have the program ask for the ``side_length`` of the 
   hexagon. Print your results in a sentence.
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           ans=3*3**(1/2)/2*side_length**2
           self.assertEqual(area,ans,feedback="Correct area")
           self.assertTrue(re.search(str(area)[:4], self.getOutput()), 'Checking answer.')
   myTests().main()