.. actex:: ex_8_6_ccs
   :author: Michael McCarrin
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: Exercises
   :topics: Strings/Exercises
   :from_source: F
   :nocodelens: 
   :pct_on_first: 0.3333333333
   :total_students_attempting: 30
   :num_students_correct: 29.0
   :mean_clicks_to_correct: 4.724137931

   Write a function that mirrors its string argument, generating a string containing the original string and the string backwards.
   ~~~~
   def mirror(mystr):
       # your code here
   
   ====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertEqual(mirror("good"),"gooddoog","Tested mirror on input of 'good'")
           self.assertEqual(mirror("Python"),"PythonnohtyP","Tested mirror on input of 'Python'")
           self.assertEqual(mirror(""),"","Tested mirror on input of ''")
           self.assertEqual(mirror("a"),"aa","Tested mirror on input of 'a'")
   
   
   myTests().main()