.. activecode:: question11_5_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 11-regex
   :subchapter: 11-escapecharacter
   :topics: 11-regex/11-escapecharacter
   :from_source: T
   :practice: T
   :nocodelens:

   Change the regex equation so that it matches with the math equation in the given string 'x'.
   ~~~~
   import re
   x = 'We learned in school today that 5 + 6 is 11!'
   y = re.findall('[0-9]+ [\D]', x)
   ====
   from unittest.gui import TestCaseGui

   class MyTests(TestCaseGui):

       def testOne(self):
           self.assertEqual(y, ['5 + 6'], "Testing that the regex equation matches correctly.")

   MyTests().main()