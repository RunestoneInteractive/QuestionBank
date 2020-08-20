.. activecode:: TL_365_ex_2_11_jcomes
   :author: Jonny Comes
   :difficulty: 1.1374386435
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :language: python
   :autograde: unittest
   :pct_on_first: 0.5
   :total_students_attempting: 6
   :num_students_correct: 6.0
   :mean_clicks_to_correct: 3.3333333333

   Write a program that will compute the area of a
   rectangle. Prompt the user to enter the width and height of the
   rectangle and store the values in variables called ``width`` and
   ``height``. Print a nice message with the answer.
   
   ~~~~
   ====
   
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertIn('input', self.getEditorText(), 'Checking that input is used.')
    self.assertIn('width', self.getEditorText(), 'Checking for variable width.')
    self.assertIn('height', self.getEditorText(), 'Checking for variable height.')
           self.assertIn(str(width*height), self.getOutput(), 'Checking answer.')
   myTests().main()