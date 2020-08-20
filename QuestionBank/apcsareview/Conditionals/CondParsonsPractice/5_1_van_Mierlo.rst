.. parsonsprob:: 5_1_van_Mierlo
   :author: Matthijs van Mierlo
   :difficulty: 0.0
   :basecourse: apcsareview
   :chapter: Conditionals
   :subchapter: CondParsonsPractice
   :topics: Conditionals/CondParsonsPractice
   :from_source: F
   :numbered: left
   :adaptive:
   :noindent:

   The following program segment should print if your guess is too low, correct, or too high  But, the blocks have been mixed up.  Drag the blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   int guess = 10;
   int answer = 5;
   =====
   if (guess < answer)
   {
   =====
       System.out.println("Your guess is too low");
   }
   =====
   else if (guess == answer)
   {
   =====
       System.out.println("You are right!");
   }
   =====
   else
   {
   =====
       System.out.println("Your guess is too high");
   }