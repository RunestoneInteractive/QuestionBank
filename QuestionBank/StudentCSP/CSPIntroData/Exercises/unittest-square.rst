.. parsonsprob:: unittest-square
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPIntroData
   :subchapter: Exercises
   :topics: CSPIntroData/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.2428571429
   :total_students_attempting: 280
   :num_students_correct: 277.0
   :mean_clicks_to_correct: 4.2960288809

   Put the code in order to define a square function which returns a value times itself.  After that function create a test class with a test using a positive number, a negative number, and 0 in that order.  The area on the left has extra blocks that are not needed in a correct solution.
   -----
   import unittest
   =====
   def square(x):
   =====
       return x * x
   =====
   class TestSquare(unittest.TestCase):
   =====
   class TestSquare(): #distractor
   =====
       def test_pos(self):
   =====
       def test_pos(): #distractor
   =====
           self.assertEqual(square(3), 9)
   =====
       def test_neg(self):
   =====
           self.assertEqual(square(-3),9)
   =====
           self.assertTrue(square(-3),9) #distractor
   =====
       def test_zero(self):
   =====
           self.assertEqual(square(0), 0)