.. parsonsprob:: ch5ex4muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 05-iterations
   :subchapter: 05-mixedupcode
   :topics: 05-iterations/05-mixedupcode
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:

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