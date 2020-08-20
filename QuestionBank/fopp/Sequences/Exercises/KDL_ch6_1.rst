.. activecode:: KDL_ch6_1
   :author: Kaelyn Leake
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: Exercises
   :topics: Sequences/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.5
   :total_students_attempting: 14
   :num_students_correct: 14.0
   :mean_clicks_to_correct: 1.8571428571

   
   
   Store the names of 5 of your ``friends`` in a list. Access the 3rd element in the list and print it in a sentence.
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertEqual(len(friends),5,feedback="Correct length for friends")
           self.assertIn('friends[2]', self.getEditorText(), 'Contains correct command')
           self.assertTrue(re.search(str(friends[2])[:2], self.getOutput()), 'Checking sentence.')
   myTests().main()