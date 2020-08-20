.. parsonsprob:: chat-labp1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: magpie-exercises
   :topics: Unit3-If-Statements/magpie-exercises
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :noindent: 
   :pct_on_first: 0.3728560776
   :total_students_attempting: 1341
   :num_students_correct: 1236.0
   :mean_clicks_to_correct: 4.0978964401

   The following program segment should print 4 random responses using if/else statements,  but the blocks have been mixed up.  Drag the blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   private String getRandomResponse()
   {
   =====
       final int NUMBER_OF_RESPONSES = 4;
       double r = Math.random();
   =====
       int whichResponse = (int)(r * NUMBER_OF_RESPONSES);
       String response = "";
   =====
       if (whichResponse == 0) {
           response = "Interesting, tell me more.";
   =====
       } else if (whichResponse == 1) {
           response = "Hmmm.";
   =====
       } else if (whichResponse == 2) {
           response = "Do you really think so?";
   =====
       } else if (whichResponse == 3) {
           response = "You don't say.";
       }
   =====
       return response;
   =====
   }