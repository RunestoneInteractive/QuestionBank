.. parsonsprob:: ch17ex5muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPStringPieces
   :subchapter: mix_stringPieces
   :topics: CSPStringPieces/mix_stringPieces
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :noindent: 
   :pct_on_first: 0.419047619
   :total_students_attempting: 105
   :num_students_correct: 76.0
   :mean_clicks_to_correct: 2.4078947368

   A restaurant needs to print out the correct total for customer #1, but all they have is a string of totals. The correct total for customer #1 is 70. The string <i>totals</i> includes the totals of the last 5 customers, separated by parentheses. Use the split and index methods to print out the proper total for customer #1. The blocks have been mixed up and include extra blocks that aren't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   totals = "31)70)43)35)80)"
   =====
   new = totals.split(")")
   =====
   new = new.split(totals) #distractor
   =====
   new = totals.split("70") #distractor
   =====
   print("Your total is: $" + new[1])
   =====
   print("Your total is: $" + new[2]) #distractor