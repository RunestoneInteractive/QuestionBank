.. parsonsprob:: unittest-sum
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPIntroData
   :subchapter: Exercises
   :topics: CSPIntroData/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.1992753623
   :total_students_attempting: 276
   :num_students_correct: 271.0
   :mean_clicks_to_correct: 6.0516605166

   Put the code in order to define the sum13 function and then the class to test the function.  The sum13 function returns the sum of the 
   numbers in a list, but doesn't include the number 13 in the sum or a number that immediately 
   follows a 13.  For the unit test, first test when the 13 is the first item in the list and then 
   when it is in the middle of the list.
   -----
   import unittest
   def sum13(nums):
   =====
       sum = 0
       found_13 = False
   =====
       for num in nums:
   =====
           if num == 13:
               found_13 = True
   =====
           elif found_13 == True:
               found_13 = False
   =====
           else:
               sum = sum + num
   =====
       return sum
   =====
   class TestSum13(unittest.TestCase):
   =====
       def test_start(self):
   =====
           self.assertEqual(sum13([13]), 0)
           self.assertEqual(sum13([13,1,2]), 2)
   =====
       def test_mid(self):
   =====
           self.assertEqual(sum13([1, 13]), 1)
           self.assertEqual(sum13([1, 13, 3, 4]), 5)
           self.assertEqual(sum13([2, 13, 13, 2, 3]), 5)
   =====
   unittest.main(verbosity=2)