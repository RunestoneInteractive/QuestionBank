.. actex:: CS152_sumBetween_loop
   :author: John Cigas
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :pct_on_first: 0.1818181818
   :total_students_attempting: 22
   :num_students_correct: 20.0
   :mean_clicks_to_correct: 7.15

   Write the function ``sumBetween(n,m)`` that returns the sum of
   all integer numbers starting at `n` and up to and
   including `m`. This uses the accumulator pattern.
   ~~~~
   
   def sumBetween(n,m):
       # your code here
   
   ====
   import re
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
   
       def testOne(self):
            editText = self.getEditorText()
            self.assertEqual(sumBetween(0,4),10,"Tested sumBetween(0,4)")
            self.assertEqual(sumBetween(1,4),10,"Tested sumBetween(1,4)")
            self.assertEqual(sumBetween(3,4),7,"Tested sumBetween(3,4)")
            self.assertEqual(sumBetween(100,100),100,"Tested sumBetween(100,100")
            self.assertEqual(1, len(re.findall("\s*for ", editText)), "Should have one for loop")
            self.assertEqual(0, len(re.findall("sum\s*\(", editText)), "Should not use sum()")
   
   
   myTests().main()