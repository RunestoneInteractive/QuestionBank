.. activecode:: KDL_ch7_5
   :author: Kaelyn Leake
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.0769230769
   :total_students_attempting: 13
   :num_students_correct: 12.0
   :mean_clicks_to_correct: 5.0833333333

   I want to calculate the area of several triangles. Using a for loop, calculate the ``area`` for all the provided dimensions (this should be a list). 
   Print your results.
   ~~~~
   base=[1,6,8,3,6,3,6,3]
   height=[4,5,7,8,9,2,4,6]
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           a=[]
           for i in range(len(base)):
               a=a+[base[i]*height[i]/2]
               self.assertIn(str(base[i]*height[i]/2)[:4], self.getOutput(), 'Checking sentence.')
           self.assertTrue(type(area)==type(a),feedback="The area should be a list")
           self.assertTrue(area==a,feedback="area values correct")
           self.assertIn('for ', self.getEditorText(), 'Contains for loop')
           
   myTests().main()