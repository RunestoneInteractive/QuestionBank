.. activecode:: KDL_ch15_1
   :author: Kaelyn Leake
   :difficulty: 1.0379592444
   :basecourse: fopp
   :chapter: AdvancedFunctions
   :subchapter: Exercises
   :topics: AdvancedFunctions/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.649122807
   :total_students_attempting: 57
   :num_students_correct: 45.0
   :mean_clicks_to_correct: 1.6444444444

   Create a function ``intadd`` that accepts two integers ``x`` and ``y``. The first integer ``x`` should have a default value of 7 and the second integer ``y`` should have a default value of 3. The function should add the two integers and return this value. 
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           
           self.assertTrue('def' in self.getEditorText(), 'function created')
           self.assertTrue(intadd(3,4)==7, '1st situation checked')
           self.assertTrue(intadd(3)==6, '2nd situation checked')
           self.assertTrue(intadd(y=4)==11, '3rd situation checked')
   
   myTests().main()