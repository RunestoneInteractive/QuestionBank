.. activecode:: KDL_exam2_2
   :author: Kaelyn Leake
   :difficulty: 1.1685823755
   :basecourse: fopp
   :chapter: Dictionaries
   :subchapter: Exercises
   :topics: Dictionaries/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.2112676056
   :total_students_attempting: 71
   :num_students_correct: 29.0
   :mean_clicks_to_correct: 3.8620689655

   Create a function ``strcount`` that accepts a string as an input and creates a dictionary that counts the number of times each letter is present in the string. The function should return the dictionary. The keys should be the letters and the values should be the number of times that letter is in the string. For example strcount('aabbcaa') would return {'a':4,'b':2,'c':1}. 
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           
           self.assertTrue('def' in self.getEditorText(), 'a function is created')
           self.assertTrue( strcount('test').keys().sort()==['t','e','s'].sort(), 'correct keys')
           self.assertTrue( strcount('abbcccdddd').values().sort()==[1,2,3,4].sort(), 'correct values')
           self.assertTrue( strcount('aabbcaa')=={'a':4,'b':2,'c':1}, 'correct dictionary')
   
   myTests().main()