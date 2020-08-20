.. activecode:: KDL_ch9_3
   :author: Kaelyn Leake
   :difficulty: 2.1676509961
   :basecourse: fopp
   :chapter: Functions
   :subchapter: Exercises
   :topics: Functions/Exercises
   :from_source: F
   :autograde: unittest
   :language: python
   :pct_on_first: 0.0588235294
   :total_students_attempting: 34
   :num_students_correct: 17.0
   :mean_clicks_to_correct: 20.8235294118

   Create a function ``cleanup`` that accepts a string makes it all lower case and breaks the string into a list at the commas, it should then strip any leading/trailing white space out of each list element, and convert any string in the list with only numbers (and periods) into a float.
   ~~~~
   alphabet='abcdefghijklmnopqrstuvwxyz '
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
   
       def testOne(self):
           def _cleanup(s):
                s=s.lower()
                l=s.split(',')
                new_list=[]
                for word in l:
                    word=word.strip()
                    let=False
                    for letter in alphabet:
                        if letter in word:
                            let=True
                    if not let:
                        word=float(word)
                    new_list+=[word]
                return new_list
           st="There is a number, 5, in this string, if you Square it it's, 25.0"
           self.assertIn('def cleanup', self.getEditorText(), 'function exists')
           self.assertEqual(type(cleanup('D')),type(_cleanup('D')), 'converts to a list') 
           self.assertEqual(cleanup('D'),_cleanup('D'), 'lower cases...')
           self.assertEqual(cleanup('14'),_cleanup('14'), 'numbers without period')
           self.assertEqual(cleanup('1.4'),_cleanup('1.4'), 'numbers with period')
           self.assertEqual(cleanup(' d '),_cleanup(' d '), 'whitespace')
           self.assertEqual(cleanup('a,b'),_cleanup('a,b'), 'splits at comma')
           self.assertEqual(cleanup(st),_cleanup(st),'function does the correct thing')
         
   myTests().main()