.. parsonsprob:: loop_centered_average-Parsons
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPWhileAndForLoops
   :subchapter: Exercises
   :topics: CSPWhileAndForLoops/Exercises
   :from_source: F
   :numbered: left

   Order the mixed up blocks below on the right side to create a function that will calculate and return a 
   "centered average".  Calculate the total of the items in the list, the lowest value, and the highest value.  
   Set the revised total to the total minus the lowest and highest values.  Set the number of items in the 
   revised total to the number of items in the list minus two.  Return the revised total divided by the 
   number of items in the revised total.  For example, get_centered_avg([1, 2, 3, 4, 100]) returns 3.  
   -----
   def centered_average(nums):
   =====
   Def centered_average(nums): #paired
   =====
       total = sum(nums)
       low = min(nums)
       high = max(nums)
   =====
       rev_total = total - low - high
   =====
       rev_total = rev_total - low - high #paired
   =====
       num_items = len(nums) - 2
   =====
       num_items = len(nums) + 2 #paired
   =====
       return rev_total / num_items
   =====
       ret rev_total / num_items #paired