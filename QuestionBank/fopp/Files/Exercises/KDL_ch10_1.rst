.. activecode:: KDL_ch10_1
   :author: Kaelyn Leake
   :difficulty: 1.6322177599
   :basecourse: fopp
   :chapter: Files
   :subchapter: Exercises
   :topics: Files/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.0611353712
   :total_students_attempting: 229
   :num_students_correct: 120.0
   :mean_clicks_to_correct: 11.7333333333

   How often does "red" and "scarlet" appear in Sir. Arthur Conan Doyle's "The Study in Scarlet". Use the scarlet.txt file to determine and return your values as ``red_count`` and ``scarlet_count``.
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           
           self.assertIn("open(", self.getEditorText(), 'Contains open for file')
           self.assertEqual(red_count, 367, "Checking value of red_count")
           self.assertEqual(scarlet_count, 2, "Checking value of scarlet_count")
   
           
   myTests().main()