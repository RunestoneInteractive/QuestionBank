.. parsonsprob:: ch17ex4muc
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
   :pct_on_first: 0.4716981132
   :total_students_attempting: 106
   :num_students_correct: 78.0
   :mean_clicks_to_correct: 1.8846153846

   The following program segment should print the integer <i>7</i> using the .find() procedure. But, the blocks have been mixed up and include extra blocks that aren't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   str = "Roads? Where we're going we don't need roads."
   =====
   pos = str.find("where") #distractor
   =====
   pos = str.find("Where")
   =====
   pos = str.find("need") #distractor
   =====
   print(pos)