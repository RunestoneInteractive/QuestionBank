.. activecode:: KDL_ch14_4
   :author: Kaelyn Leake
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: MoreAboutIteration
   :subchapter: Exercises
   :topics: MoreAboutIteration/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.4117647059
   :total_students_attempting: 34
   :num_students_correct: 22.0
   :mean_clicks_to_correct: 1.7272727273

   Use turtle (and the coding example in the reading...) to draw a random turtle path on screen. Modify the code so that the turtle stops if it goes outside of the area described by a circle of a given radius. The code you wrote for the monte carlo simulation might be helpful...
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertIn('while', self.getEditorText(), 'Contains while loop')
           self.assertIn('import turtle', self.getEditorText(), 'turtle!')
           self.assertIn('import random', self.getEditorText(), 'Contains random')
   
           
   myTests().main()