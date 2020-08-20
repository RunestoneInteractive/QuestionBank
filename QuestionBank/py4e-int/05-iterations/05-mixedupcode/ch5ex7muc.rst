.. parsonsprob:: ch5ex7muc
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

   The following program segment should calculate the sum of all odd numbers between 0 and 30. Start by initializing the variable <i>sum</i> and loop through the odd numbers. The blocks have been mixed up and include an extra block that isn't needed in the solution. Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   sum = 0
   =====
   numbers = range(1,30,2)
   =====
   numbers = range(0,29,2) #distractor
   =====
   for number in numbers:
   =====
       sum = sum + number
   =====
   print(sum)