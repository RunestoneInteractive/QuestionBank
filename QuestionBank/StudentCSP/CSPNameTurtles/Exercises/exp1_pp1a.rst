.. parsonsprob:: exp1_pp1a
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPNameTurtles
   :subchapter: Exercises
   :topics: CSPNameTurtles/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.1067961165
   :total_students_attempting: 103
   :num_students_correct: 101.0
   :mean_clicks_to_correct: 7.5148514851

   Put the blocks in order to define the function has22 to return True if there are at least two items in the list nums that are adjacent and both equal to 2, otherwise return False. For example, return True for [1, 2, 2] since there are two adjacent items equal to 2 (at index 1 and 2) and False for [2, 1, 2] since the 2’s are not adjacent.
   -----
   def has22(nums):
   =====
       i = 1
   =====
       i = 0 #distractor
   =====
       while i < len(nums):
   =====
           if nums[i] == 2 and nums[i-1] == 2:
   =====
           if nums[i] == 2 and nums[i+1] == 2: #distractor
   =====
               return True
   =====
               return true #distractor
   =====
           i += 1
   =====
       return False