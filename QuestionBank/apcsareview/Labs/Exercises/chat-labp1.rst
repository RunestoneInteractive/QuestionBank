.. parsonsprob:: chat-labp1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Labs
   :subchapter: Exercises
   :topics: Labs/Exercises
   :from_source: T
   :numbered: left
   :adaptive:
   :noindent:

   The following program segment should print if your guess is too low, correct, or too high  But, the blocks have been mixed up.  Drag the blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
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