.. activecode:: KDL_ch12_3
   :author: Kaelyn Leake
   :difficulty: 1.5227576975
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.0
   :total_students_attempting: 11
   :num_students_correct: 8.0
   :mean_clicks_to_correct: 9.875

   I'm a fan of a good game of tic-tac-toe. Write two functions one that draws a ``circle`` and one that draws an ``X`` using turtle. The functions should accept an x and y value and use that as the center of the shape. Then use a for loop with user input to create a basic tic-tac-toe game. You'll need to alternate between drawing X and O. Note: There are at most 5 turns for 1 player and 4 for the second or 9 total. Take advantage of the circle code you've made before!!! Will manually grade the output is correct....
   ~~~~
   import sys
   sys.setExecutionLimit(60000*5) #5 mins
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           
           self.assertIn('for ', self.getEditorText(), 'Contains for loop')
           self.assertIn('import turtle', self.getEditorText(), 'turtle used')
           self.assertIn('def circle', self.getEditorText(), 'function exists')
           self.assertIn('def X', self.getEditorText(), 'function exists')  
           self.assertIn('input', self.getEditorText(), 'Contains input in loop')
         
   myTests().main()