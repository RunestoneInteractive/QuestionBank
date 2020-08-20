.. activecode:: question11_8_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 11-regex
   :subchapter: 11-debugging
   :topics: 11-regex/11-debugging
   :from_source: T
   :practice: T
   :nocodelens:

   Fix the regex equation so that the code matches any dollar sign ($) followed by an integer or float.
   ~~~~
   import re
   x = 'The apples cost $9.99, whereas the bananas were only $5 and the oranges were $2.50 each.'
   y = re.findall('$[0_9\.]', x)

   ====
   from unittest.gui import TestCaseGui

   class MyTests(TestCaseGui):

       def testOne(self):
           self.assertEqual(y, ['$9.99', '$5', '$2.50'], "Testing that the regex equation matches the proper parts of the string.")

   MyTests().main()