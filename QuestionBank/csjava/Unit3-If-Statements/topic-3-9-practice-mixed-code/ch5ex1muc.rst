.. parsonsprob:: ch5ex1muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-9-practice-mixed-code
   :topics: Unit3-If-Statements/topic-3-9-practice-mixed-code
   :from_source: F
   :numbered: left
   :practice: T
   :adaptive:
   :noindent:

   The following program segment should print if your guess is too low, correct, or too high  But, the blocks have been mixed up.  Drag the blocks from the left and put them in the correct order on the right.

   -----
   int guess = 10;
   int answer = 5;
   =====
   if (guess < answer)
   =====
   {
       System.out.println("Your guess is too low");
   }
   =====
   else if (guess == answer)
   =====
   {
       System.out.println("You are right!");
   }
   =====
   else
   =====
   {
        System.out.println("Your guess is too high");
   }