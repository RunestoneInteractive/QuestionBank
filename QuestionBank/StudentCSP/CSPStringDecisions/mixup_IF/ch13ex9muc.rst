.. parsonsprob:: ch13ex9muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPStringDecisions
   :subchapter: mixup_IF
   :topics: CSPStringDecisions/mixup_IF
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :pct_on_first: 0.3513513514
   :total_students_attempting: 37
   :num_students_correct: 29.0
   :mean_clicks_to_correct: 4.0

   The following program segment should ask whether the user wants to terminate the program and print out the appropriate statement based on the user's response. The blocks have been mixed up and include extra blocks that aren't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   response = input("Would you like to terminate the program? (Y/N)")
   =====
   if response == "Y":
   =====
   if input = "Y": #paired
   =====
       print("The program is now ending.")
   =====
   elif response == "N":
   =====
   elif input = "N": #paired
   =====
       print("The program will continue to run.")