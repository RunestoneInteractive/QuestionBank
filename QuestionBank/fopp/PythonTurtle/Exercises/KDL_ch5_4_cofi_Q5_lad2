.. activecode:: KDL_ch5_4_cofi_Q5_lad2
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

   Use the turtle module to draw a Z in green. 
   The top and bottom of the Z should each be 50 long and the diagonal of the T should be 75 long. 
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           
           self.assertIn('import turtle', self.getEditorText(), 'Contains Turtle module')
           self.assertIn('green', self.getEditorText(), 'green in code')
           self.assertIn('50', self.getEditorText(), '50 in code')
           self.assertIn('75', self.getEditorText(), '75 in code')
   
           
   myTests().main()