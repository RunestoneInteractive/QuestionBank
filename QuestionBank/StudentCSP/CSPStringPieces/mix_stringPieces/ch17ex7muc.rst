.. parsonsprob:: ch17ex7muc
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
   :pct_on_first: 0.07
   :total_students_attempting: 100
   :num_students_correct: 67.0
   :mean_clicks_to_correct: 5.2089552239

   The following function should take in two strings as arguments, then print and return the position of the first parameter in the second string. The blocks have been mixed up and include an extra block that isn't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   def stringPos(phrase, sentence):
   =====
       pos = sentence.find(phrase)
   =====
       pos = phrase.find("sentence") #distractor
   =====
       print(pos)
   =====
       return pos