.. parsonsprob:: 7_6_1_Print-Sum-Evens
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPRepeatNumbers
   :subchapter: print
   :topics: CSPRepeatNumbers/print
   :from_source: T
   :pct_on_first: 0.0551181102
   :total_students_attempting: 1270
   :num_students_correct: 1178.0
   :mean_clicks_to_correct: 4.9252971138

   The following is the correct code for printing the value of number and the sum each time through the loop, but it is mixed up. The code should initialize the accumulator, create the list of numbers, and then loop through the list of numbers.  Each time through the loop it should print the value of number, add the value of number to the accumulator, and then print the current sum.  Drag the blocks from the left and put them in the correct order on the right.  Don't forget to indent blocks in the body of the loop.  Just drag the block further right to indent.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   sum = 0
   =====
   numbers = range(0,101,2)
   =====
   for number in numbers:
   =====
       print("Number:",number)
   =====
       sum = sum + number
   =====
       print(sum)