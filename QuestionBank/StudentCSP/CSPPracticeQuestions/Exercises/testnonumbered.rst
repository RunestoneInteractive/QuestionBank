.. parsonsprob:: testnonumbered
   :author: Nelson Yang
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPPracticeQuestions
   :subchapter: Exercises
   :topics: CSPPracticeQuestions/Exercises
   :from_source: F
   :adaptive: 
   :pct_on_first: 0.0714285714
   :total_students_attempting: 28
   :num_students_correct: 19.0
   :mean_clicks_to_correct: 11.1052631579

   Put the code below in order to print information from a list of numbers: the sum, the maximum, the minimum, and if there is a least one number in the list the average.
   -----
   def printInfo(nums):
   =====
       total = sum(nums)
   =====
       print(total)
   =====
       print(max(nums))
   =====
       print(min(nums))
   =====
       if len(nums) > 0:
   =====
           print(total / len(nums))
   
   fig values (conf.py):
   
   arsons_div_class - custom CSS class of the component's outermost div