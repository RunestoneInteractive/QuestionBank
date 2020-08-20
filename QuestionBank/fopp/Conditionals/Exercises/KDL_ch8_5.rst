.. activecode:: KDL_ch8_5
   :author: Kaelyn Leake
   :difficulty: 1.0330209728
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: Exercises
   :topics: Conditionals/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.3904761905
   :total_students_attempting: 105
   :num_students_correct: 66.0
   :mean_clicks_to_correct: 1.5606060606

   Use an if statement to print "big" if a value is greater than 100 and "small" if a value is less than 10 otherwise print "middle". Check the value of a variable ``x``. Make sure your code gets pass for all three situations! 
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           def checkval(k):
              if x >100:
                  val="big"
              elif x<10:
                  val="small"
              else:
                  val='middle'
              return val
           self.assertIn(checkval(x), self.getOutput(), 'Contains correct print')
           self.assertIn('if', self.getEditorText(), 'Contains if statement')
          
           
   myTests().main()