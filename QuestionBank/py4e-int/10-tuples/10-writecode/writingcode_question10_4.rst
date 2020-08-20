.. activecode:: writingcode_question10_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 10-tuples
   :subchapter: 10-writecode
   :topics: 10-tuples/10-writecode
   :from_source: T
   :nocodelens:
   :practice: T

   pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}

   ====
   from unittest.gui import TestCaseGui

   class MyTests(TestCaseGui):

       def testOne(self):
           self.assertEqual(p_names, ['Rattata', 'Machop', 'Seel', 'Volbeat', 'Solrock'], "Testing that p_name has the correct values.")
           self.assertEqual(p_number, [19, 66, 86, 86, 126], "Testing that p_number has the correct values.")

   MyTests().main()