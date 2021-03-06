.. tabbed:: exp1_q1
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameNumbers
   :subchapter: Exercises
   :topics: CSPNameNumbers/Exercises
   :from_source: F

   .. tab:: Parsons Problem

      .. parsonsprob:: exp1_pp1
         :numbered: left
         :adaptive:

         Put the blocks in order to define the has22 function that returns True if there are at least two adjacent items that are both equal to 2, otherwise it returns False.
         -----
         def has22(nums):
         =====
             i = 1
         =====
             while i < len(nums):
         =====
                 if nums[i] == 2 and nums[i-1] == 2:
         =====
                     return True
         =====
                 i += 1
         =====
             return False

   .. tab:: Write Code Problem

      .. activecode:: exp1_q1_write
         :autograde: unittest
         :nocodelens: 

         Finish the function below to return True if there are at least two items in the list nums that are adjacent and both equal to 2, otherwise return False
   
         ~~~~
         def has22(nums):

         ====
         from unittest.gui import TestCaseGui

         class myTests(TestCaseGui):

             def testOne(self):
                 self.assertEqual(has22[1, 2, 2], True)
                 self.assertEqual(has22[1, 2, 1, 2], False)
                 self.assertEqual(has22[2, 1, 2], False)
                 self.assertEqual(has22[2, 2, 1], True)
                 self.assertEqual(has22[3, 4, 2], False)
                 self.assertEqual(has22[2], False)
                 self.assertEqual(has22[], False)
              
         myTests().main()