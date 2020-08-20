.. parsonsprob:: ch3ex3muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPNameNumbers
   :subchapter: VariablePracticeParsons
   :topics: CSPNameNumbers/VariablePracticeParsons
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :noindent: 
   :pct_on_first: 0.4157480315
   :total_students_attempting: 635
   :num_students_correct: 613.0
   :mean_clicks_to_correct: 2.5334420881

   The following program segment should print the amount of punch left in a two gallon punch bowl if 12oz is poured into as many cups as possible. One gallon contains 128oz and the punch bowl is full. But, the blocks have been mixed up and include an extra block that isn't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   oInGallon = 128
   oInCup = 12
   =====
   totalPunch = 2 * oInGallon
   =====
   amountLeft = totalPunch % oInCup
   =====
   print(amountLeft)
   =====
   amountLeft = totalPunch / oInCup #distractor