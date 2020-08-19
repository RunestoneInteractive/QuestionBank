.. activecode:: writingcode_question10_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 10-tuples
   :subchapter: 10-writecode
   :topics: 10-tuples/10-writecode
   :from_source: T
   :practice: T
   :nocodelens:

   majors = {3084: 'Computer Science', 3025: 'Electrical Engineering', 3020: 'Computer Engineering', 3027: 'Cybersecurity', 3068: 'Biometric Systems Engineering'}

   ====
   from unittest.gui import TestCaseGui

   class MyTests(TestCaseGui):

       def testOne(self):
           self.assertEqual(find_major(3084),(3084, 'Computer Science'), "Checking that 'Computer Science' is associated with 3084.")
           self.assertEqual(find_major(0), (None, 'Error'), "Making sure that major code 0 returns Error.")

   MyTests().main()