.. parsonsprob:: ch13ex10muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPStringDecisions
   :subchapter: mixup_IF
   :topics: CSPStringDecisions/mixup_IF
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :pct_on_first: 0.1142857143
   :total_students_attempting: 35
   :num_students_correct: 27.0
   :mean_clicks_to_correct: 5.9259259259

   The following program segment should ask the user to first input two numbers which will serve as parameters, then ask for a third number and determine whether it falls within the range of the first two numbers. The blocks have been mixed up and include extra blocks that aren't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   first = input("Enter the first number parameter: ")
   second = input("Enter the second number parameter: ")
   =====
   num = input("Enter a number: ")
   =====
   if num > first and num < second or num < first and num > second:
   =====
   if num > first or num < second and num < first or num > second: #distractor
   =====
       print("Your number falls in the given range")
   =====
   else:
   =====
       print("Your number does not fall in the given range")