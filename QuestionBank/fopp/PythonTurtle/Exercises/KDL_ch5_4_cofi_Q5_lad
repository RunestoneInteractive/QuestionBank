.. activecode:: KDL_ch5_4_cofi_Q5_lad
   :author: Lynda Danielson
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: PythonTurtle
   :subchapter: Exercises
   :topics: PythonTurtle/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   Use the turtle module to draw a T in blue. 
   The top of the T should be 100 long and the height of the T should be 125 long. 
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           
           self.assertIn('import turtle', self.getEditorText(), 'Contains Turtle module')
           self.assertIn('blue', self.getEditorText(), 'blue in code')
           self.assertIn('100', self.getEditorText(), '100 in code')
           self.assertIn('125', self.getEditorText(), '125 in code')
   
           
   myTests().main()