.. activecode:: KDL_ch7_4
   :author: Kaelyn Leake
   :difficulty: 1.0453094429
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: Exercises
   :topics: Iteration/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.3846153846
   :total_students_attempting: 13
   :num_students_correct: 13.0
   :mean_clicks_to_correct: 1.7692307692

   I'm lazy! I want to write emails to all my students with the same (but personalized) message with their ``names`` included. Make sure to include at least 5 names. Use a for loop to write messages to all the students in the list.
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertTrue(len(names)>=5,feedback="names is long enough")
           self.assertIn('for ', self.getEditorText(), 'Contains for loop')
           for x in names:
               self.assertIn(x, self.getOutput(), 'Checking sentence.')
   myTests().main()