.. parsonsprob:: ch88ex8muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPWhileAndForLoops
   :subchapter: mixup_WhileAndFor
   :topics: CSPWhileAndForLoops/mixup_WhileAndFor
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :pct_on_first: 0.1012658228
   :total_students_attempting: 158
   :num_students_correct: 143.0
   :mean_clicks_to_correct: 2.6153846154

   The following program should find the sum of every multiple of 3 between 3 and 36 and print the sum after each addition.  But, the blocks have been mixed up and include an extra block that isn't needed in the solution. Drag the needed blocks from the left and put them in the correct order on the right. Click the <i>Check Me</i> button to check your solution.</p>
   -----
   sum = 0
   =====
   numbers = range(3, 37, 3)
   =====
   for number in numbers:
   =====
       sum = sum + number
   =====
       print(sum)
   =====
       print(number) #distractor