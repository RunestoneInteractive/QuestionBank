.. activecode:: KDL_exam2_3
   :author: Kaelyn Leake
   :difficulty: 1.1234142921
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.5833333333
   :total_students_attempting: 24
   :num_students_correct: 21.0
   :mean_clicks_to_correct: 3.0952380952

   Create a function called ``key_val`` that accepts a dictionary and a list of keys and returns the corresponding list of values. For example key_val({'one':1,'two':2,'three':3,'four':4},['one','three','two']) should return [1,3,2].
   ~~~~
   #your code here!
   print(key_val({'one':1,'two':2,'three':3,'four':4},['one','three','two']))
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertTrue('key_val' in globals(), 'key_val exists')
           self.assertTrue('def' in self.getEditorText(), 'function created')
           self.assertTrue( key_val({'one':1,'two':2,'three':3,'four':4},['one','three','two'])==[1,3,2], 'returns correct value')
           self.assertTrue( key_val({'one':3,'two':4,'three':6,'four':7},['one','three','two'])==[3,6,4], "returns another correct value - this is to verify you aren't hard coding....")
   
   myTests().main()