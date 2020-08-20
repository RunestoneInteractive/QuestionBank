.. parsonsprob:: ch88ex4muc
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
   :pct_on_first: 0.0609756098
   :total_students_attempting: 164
   :num_students_correct: 144.0
   :mean_clicks_to_correct: 10.1666666667

   The following program segment should result in an infinite loop. But the blocks have been mixed up and include an extra block that ins't needed in the solution. Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   def loopMe(first, second):
   =====
       while first > second:
   =====
       while first == second: #distractor
   =====
           print('Am I infinitely looping?')
   =====
       return True
   =====
   loopMe(7, 4)
   =====
   loopMe(1, 3) #distractor