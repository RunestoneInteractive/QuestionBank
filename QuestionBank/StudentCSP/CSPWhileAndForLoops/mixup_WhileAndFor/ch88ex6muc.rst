.. parsonsprob:: ch88ex6muc
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
   :pct_on_first: 0.4350649351
   :total_students_attempting: 154
   :num_students_correct: 138.0
   :mean_clicks_to_correct: 2.6884057971

   The following program segment should calculate and print the sum of all numbers between 0 and 30. Start by initializing the variable <i>sum</i>. The blocks have been mixed up and include an extra block that ins't needed in the solution. Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   sum = 0
   =====
   numbers = range(31)
   =====
   numbers = range(30) #distractor
   =====
   for number in numbers:
   =====
       sum = sum + number
   =====
   print(sum)