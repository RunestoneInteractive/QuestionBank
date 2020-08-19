.. activecode:: KDL_ch10_2
   :author: Kaelyn Leake
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Files
   :subchapter: Exercises
   :topics: Files/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.0421052632
   :total_students_attempting: 95
   :num_students_correct: 35.0
   :mean_clicks_to_correct: 11.7714285714

   Using altair, plot a histogram of lengths of the words in the words5000.csv file. Your lengths should be saved in a list called ``list_len`` and passed to altair.
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           wordlist=open('words5000.csv','r')
           lengths=[]
           wordlist.readline()
           for line in wordlist.readlines():
                s=line.split(',')
                lengths+=[len(s[1])]
           self.assertIn("open(", self.getEditorText(), 'Contains open for file')
           self.assertIn("import altair", self.getEditorText(), 'Using altair')
           self.assertEqual(lengths, list_len, "Testing the list_len values.")
           
   myTests().main()