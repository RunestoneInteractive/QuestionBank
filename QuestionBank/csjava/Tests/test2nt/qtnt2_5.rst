.. mchoice:: qtnt2_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Tests
   :subchapter: test2nt
   :topics: Tests/test2nt
   :from_source: T
   :answer_a: hciwdnas
   :answer_b: sandwich
   :answer_c: andwichandwichndwichdwichwichichchh
   :answer_d: hchichwichdwichndwichandwich
   :answer_e: Nothing is printed because an infinite loop occurs
   :correct: a
   :feedback_a: The recursive call occurs until the length of s equals 0, then the letters of the word are printed in reverse order.
   :feedback_b: This would occur if the print statement came before the recursive call. Because the compiler works through the recursive call before moving to the other statements, the letters are printed in reverse order.
   :feedback_c: This would occur if the print statement came before the recursive call and included s.substring(1), not s.substring(0, 1). The statements are printed after the recursive call is made, so the compiler works through every recursive call before it prints out the letters, and the letters are printed in reverse order.
   :feedback_d: This would occur if the print statement included s.substring(1). Each call of the printString method prints only one letter at a time, because the substring that is printed is s.substring(0,1).
   :feedback_e: This method ends when s.length() equals zero, so the base case is reached after eight passes for the word "sandwich". An infinite loop will not occur.

   Consider the method ``printString`` shown below. What is printed as a result of printString("sandwich")?

   .. code-block:: java

      public void printString(String s)
      {
         if (s.length() > 0)
         {
            printString(s.substring(1));
            System.out.print(s.substring(0, 1));
         }
      }