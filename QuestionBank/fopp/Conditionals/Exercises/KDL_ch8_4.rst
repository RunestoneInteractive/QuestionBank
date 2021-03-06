.. activecode:: KDL_ch8_4
   :author: Kaelyn Leake
   :difficulty: 1.0642570281
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: Exercises
   :topics: Conditionals/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.5833333333
   :total_students_attempting: 12
   :num_students_correct: 11.0
   :mean_clicks_to_correct: 2.0909090909

   Imagine you own a pizza place. You have a system that checks a list of ``requested_toppings`` to see if they are available. Make a list of ``available_toppings`` and use a for loop and a if statement to determine which requested toppings aren't in the available list. Print the toppings that aren't available.  
   
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           for toppy in requested_toppings:
               if toppy not in available_toppings:
                   self.assertIn(toppy, self.getOutput(), 'correct toppings not available')
           self.assertIn('if ', self.getEditorText(), 'Contains if statement')
           self.assertIn('print(', self.getEditorText(), 'Contains print')
           self.assertIn('for', self.getEditorText(), 'Contains print')
           
   myTests().main()