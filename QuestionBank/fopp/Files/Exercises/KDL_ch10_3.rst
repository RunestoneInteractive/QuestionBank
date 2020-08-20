.. activecode:: KDL_ch10_3
   :author: Kaelyn Leake
   :difficulty: 1.4123159304
   :basecourse: fopp
   :chapter: Files
   :subchapter: Exercises
   :topics: Files/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.0
   :total_students_attempting: 65
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 8.0

   Using words5000.csv and scarlet.csv . Determine the counts for each part of speech in the story. The counts should be stored in a variable ``part_count`` and the parts of speech should be stored in a variable ``part_o_speech``, they should be in the order the appear in the word list. Plot the histogram using altair. If the word isn't in the 5000 word list skip it in the count.  
   ~~~~
   
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           strcmp=['a','v','c','i','t','p','d','x','r','m','n','e','j','u']
           self.assertEqual(part_o_speech,strcmp, 'part of speech correct')
           strcmp=[4375,3489,4257,6205,1010,4099,2090,170,5216,395,4804,130,2013,134]
           self.assertEqual(part_count,strcmp, "part count correct ---doesn't need to be exactly the same but should be similar.")
           self.assertIn("open(", self.getEditorText(), 'Contains open for file')
           self.assertIn("import altair", self.getEditorText(), 'Using altair')
   
   myTests().main()