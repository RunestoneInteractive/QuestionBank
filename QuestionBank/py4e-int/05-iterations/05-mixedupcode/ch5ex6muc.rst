.. parsonsprob:: ch5ex6muc
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