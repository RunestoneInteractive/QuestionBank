.. parsonsprob:: midtermCountEvens2
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPPracticeQuestions
   :subchapter: Exercises
   :topics: CSPPracticeQuestions/Exercises
   :from_source: F
   :adaptive:
   :numbered: left

   Put the code below in order to return how many even numbers are in the list nums.
   -----
   def count_evens(nums):
   =====
       total = 0
   =====
       for num in nums:
   =====
           if num % 2 == 0:
   =====
               total += 1
   =====
       return total

config values (conf.py):

- parsons_div_class - custom CSS class of the component's outermost div