.. parsonsprob:: exp1_pp1
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPNameNumbers
   :subchapter: Exercises
   :topics: CSPNameNumbers/Exercises
   :from_source: F
   :numbered: left
   :adaptive:

   Put the blocks in order to define a has22 function that returns True if there are at least two adjacent items that are both equal to 2, otherwise it returns False.  For example, it should return True for [1, 2, 2] since two items that are both equal to 2 are adjacent (at index 1 and 2) and should return false for [2, 1, 2] since the 2's are not adjacent.
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