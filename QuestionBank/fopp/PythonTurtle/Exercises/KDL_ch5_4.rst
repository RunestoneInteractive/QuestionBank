.. activecode:: KDL_ch5_4
   :author: Kaelyn Leake
   :difficulty: 1.0610838415
   :basecourse: fopp
   :chapter: PythonTurtle
   :subchapter: Exercises
   :topics: PythonTurtle/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.329787234
   :total_students_attempting: 94
   :num_students_correct: 54.0
   :mean_clicks_to_correct: 2.037037037

   Use the turtle module to draw an L. The side of the L should be 100 long and the width of the L should be 75 long. The top left should start at :math:`x=-100`, :math:`y=100`.
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           
           self.assertIn('import turtle', self.getEditorText(), 'Contains Turtle module')
           self.assertIn('100', self.getEditorText(), '100 in code')
           self.assertIn('75', self.getEditorText(), '75 in code')
   
           
   myTests().main()