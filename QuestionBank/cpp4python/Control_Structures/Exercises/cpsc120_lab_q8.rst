.. parsonsprob:: cpsc120_lab_q8
   :author: Matthew Zuniga
   :difficulty: 0.0
   :basecourse: cpp4python
   :chapter: Control_Structures
   :subchapter: Exercises
   :topics: Control_Structures/Exercises
   :from_source: F

   Use a <b>nested for-loop</b> to construct the multiplication table starting from 1 to 10.
   <br>
   <br>
   Sample Output: <br>
   1 2 3 4 5 . . .<br>
   2 4 6 8 10 . . . <br>
   etc 
   -----
   for(int i = 1; i <= 10; i++) {
   =====
    for(int j = 1; j <= 10; j++) {
   =====
     cout << i * j << " ";
   =====
    }
   =====
   }
   =====
   #distractorfor(int i: j) {
   =====
   #distractorfor(int i = 0; i < 10; i++) {
   =====
   #distractor for(int j = 0; j < 10; j++) {