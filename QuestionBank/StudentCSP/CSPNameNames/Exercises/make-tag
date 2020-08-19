.. activecode:: make-tag
       :author: Barbara  Ericson
       :difficulty: 0.0
       :basecourse: StudentCSP
       :chapter: CSPNameNames
       :subchapter: Exercises
       :topics: CSPNameNames/Exercises
       :from_source: F
       :nocodelens: 
       :autograde: unittest
       :pct_on_first: 0.4038461538
       :total_students_attempting: 52
       :num_students_correct: 47.0
       :mean_clicks_to_correct: 2.8085106383

       The web is built with HTML strings like "<i>Yay</i>" which draws Yay 
       as italic text. In this example, the "i" tag makes <i> and </i> which surround 
       the word "Yay". Given tag and word strings, create the HTML string with tags 
       around the word.  For example, make_tags('i', 'Yay') returns '<i>Yay</i>'.
       ~~~~
       def make_tags(tag,word):
       
       ====
       from unittest.gui import TestCaseGui
       
       class myTests(TestCaseGui):
       
           def testOne(self):
               self.assertEqual(make_tags('i', 'Yay'), '<i>Yay</i>', "make_tags('i', 'Yay')")
               self.assertEqual(make_tags('i', 'Hello'), '<i>Hello</i>', "make_tags('i', 'Hello')")
               self.assertEqual(make_tags('b', 'Yay'), '<b>Yay</b>', "make_tags('b', 'Yay')")
               self.assertEqual(make_tags('i', 'i'), '<i>i</i>', "make_tags('i', 'i')")
               self.assertEqual(make_tags("i", ""), "<i></i>", 'make_tags("i", "")')
       
       
       myTests().main()