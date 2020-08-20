.. parsonsprob:: loop_sum_odd_parsons
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPWhileAndForLoops
   :subchapter: Exercises
   :topics: CSPWhileAndForLoops/Exercises
   :from_source: F
   :adaptive:
   :numbered: left

   Put the code blocks in order to return the sum of all of the odd numbers in the list nums.  
   For example, sum_odd([1,1,1]) returns 3 and sum_odd([2,4]) returns 0.
   -----
   def sum_odd(num_list):
   =====
   def sum_odd(num_list) #paired
   =====
       total = 0
   =====
       for num in num_list:
   =====
           if num % 2 == 1:
   =====
           if num % 2 == 0: #paired
   =====
               total += num
   =====
       return total
   =====
       return sum #paired