.. activecode:: KDL_exam2_4
   :author: Kaelyn Leake
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Files
   :subchapter: Exercises
   :topics: Files/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.0
   :total_students_attempting: 40
   :num_students_correct: 10.0
   :mean_clicks_to_correct: 14.7

   I've created a file called ``exam2_file.txt`` (shown above) use python to open the file and create lists called ``tall`` and ``short`` from the supplied file. You should end up with tall=['Great Dane', 'Tiger', 'Giraffe', 'Whale Shark'] and short=['Weiner Dog', 'House Cat', 'Okapi', 'Dwarf lanternshark'].
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertTrue('exam2_file.txt' in self.getEditorText(), "Code uses 'exam2_file.txt'")
           self.assertTrue('open' in self.getEditorText(), 'File opened')
           self.assertTrue( '.read' in self.getEditorText(), 'something read from file')
           self.assertTrue( tall== ['Great Dane','Tiger','Giraffe','Whale Shark'], 'tall correct')
           self.assertTrue( short== ['Weiner Dog', 'House Cat', 'Okapi', 'Dwarf lanternshark'], 'short correct')
           self.assertTrue("'Great Dane','Tiger','Giraffe','Whale Shark'" not in self.getEditorText() and "'Weiner Dog', 'House Cat', 'Okapi', 'Dwarf lanternshark'" not in self.getEditorText(), 'Not hard coded')
   myTests().main()