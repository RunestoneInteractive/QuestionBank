.. activecode:: KDL_exam2_5
   :author: Kaelyn Leake
   :difficulty: 1.4146720214
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: Exercises
   :topics: TransformingSequences/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.1170212766
   :total_students_attempting: 94
   :num_students_correct: 50.0
   :mean_clicks_to_correct: 8.04

   You are supplied with a string ``s`` below. Using python and not hard coding...Remove white space from the beginning and end, make the string lower case and replace all the words 'cat' with 'dog'. This new string should be saved as ``newS``. The final string should look like newS='the dog ate the dog food, it was yummy!'
   
   ~~~~
   s=' The cat ate the dog food, it was YUMMY!  '
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertTrue('newS' in globals(),'newS has been created')
           self.assertTrue(newS==s.strip().lower().replace('cat','dog'), 'Correct string created')
           self.assertTrue('the dog ate the dog food, it was yummy!' not in self.getEditorText(), 'The string was not hard coded')
   
   myTests().main()