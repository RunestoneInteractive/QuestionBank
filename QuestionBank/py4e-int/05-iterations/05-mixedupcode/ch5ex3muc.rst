.. parsonsprob:: ch5ex3muc
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

   The following program segment should print all even numbers from 0 to 8 (this includes 0 and 8). But the blocks have been mixed up and include an extra block that isn't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   def skipCount(start, increment, stop):
   =====
       counter = start
   =====
       while counter < stop:
   =====
           print(counter)
   =====
           counter += increment
   =====
       return counter
   =====
   print(skipCount(0,2,9))
   =====
   print(skipCount(0,2,8)) #distractor