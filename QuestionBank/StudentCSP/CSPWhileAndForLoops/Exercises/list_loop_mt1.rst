.. parsonsprob:: list_loop_mt1
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPWhileAndForLoops
   :subchapter: Exercises
   :topics: CSPWhileAndForLoops/Exercises
   :from_source: F
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.5744680851
   :total_students_attempting: 282
   :num_students_correct: 281.0
   :mean_clicks_to_correct: 2.5836298932

   Put the code blocks in order to define a function total_odd that returns the sum of the odd 
   numbers in the passed list.
   -----
   def total_odd(nums):
   =====
      total = 0
   =====
      for num in nums:
   =====
      for num in nums #paired
   =====
          if num % 2 == 1:
   =====
          if nums % 2 == 0: #paired
   =====
              total = total + num
   =====
              total = total + 1 #paired
    =====
      return total
    =====
      ret total #paired