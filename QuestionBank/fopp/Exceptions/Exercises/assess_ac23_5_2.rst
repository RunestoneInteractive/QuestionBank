.. actex:: assess_ac23_5_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Exceptions
   :subchapter: Exercises
   :topics: Exceptions/Exercises
   :from_source: T
   :practice: T
   :autograde: unittest

   The code below assigns the 5th letter of each word in ``food`` to the new list ``fifth``. However, the code currently produces errors. Insert a try/except clause that will allow the code to run and produce of list of the 5th letter in each word. If the word is not long enough, it should not print anything out. Note: The ``pass`` statement is a null operation; nothing will happen when it executes.
   ~~~~

   food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
   fifth = []

   for x in food:
       fifth.append(x[4])

   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def testOneA(self):
           self.assertEqual(fifth, ['o', 'k', 'w', 't', 'n'], "Testing that fifth is assigned to correct values.")

    myTests().main()