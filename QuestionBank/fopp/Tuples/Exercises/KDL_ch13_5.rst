.. activecode:: KDL_ch13_5
   :author: Kaelyn Leake
   :difficulty: 1.0050487665
   :basecourse: fopp
   :chapter: Tuples
   :subchapter: Exercises
   :topics: Tuples/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.7619047619
   :total_students_attempting: 42
   :num_students_correct: 35.0
   :mean_clicks_to_correct: 1.0857142857

   Create a function ``tuplize`` that accepts two inputs and returns them in a tuple. The first input and then the second.
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           
           self.assertTrue('def' in self.getEditorText(), 'function defined')
           self.assertTrue(tuplize(1,2)==(1,2), '1st situation checked')
           self.assertTrue(tuplize('cat','dog')==('cat','dog'), '2nd situation checked')
   
   myTests().main()