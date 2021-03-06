.. activecode:: access_ac_2_1_1_11
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: week2a1
   :topics: Sequences/week2a1
   :from_source: T
   :language: python
   :autograde: unittest
   :practice: T

   Assign the last element of ``lst`` to the variable ``end_elem``. Do this so that it works no matter how long lst is.
   ~~~~
   lst = ["hi", "goodbye", "python", "106", "506", 91, ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 109, "chair", "pizza", "wolverine", 2017, 3.92, 1817, "account", "readings", "papers", 12, "facebook", "twitter", 193.2, "snapchat", "leaders and the best", "social", "1986", 9, 29, "holiday", ["women", "olympics", "gold", "rio", 21, "2016", "men"], "26trombones"]

   =====

   from unittest.gui import TestCaseGui
   import re

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(end_elem, lst[-1], "Testing that end_elem has the correct element assigned.")
         self.assertFalse(re.search(r'end_elem\s*=\s*\S26trombones\S', self.getEditorText()), "Hardcoding Check (Don't worry about actual and expected values)")

   myTests().main()