.. parsonsprob:: countEs
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit4-Iteration
   :subchapter: topic-4-3-strings-loops
   :topics: Unit4-Iteration/topic-4-3-strings-loops
   :from_source: F
   :numbered: left
   :practice: T
   :adaptive:
   :noindent:

   The following main method has the correct code to count the number of e's in a string, but the code is mixed up.  Drag the blocks from the left area into the correct order in the right area.  Click on the "Check Me" button to check your solution.
   -----
   public static void main(String[] args)
   {
   =====
      String message = "e is the most frequent English letter.";
      int count = 0;
   =====
      for(int i=0; i < message.length(); i++)
      {
   =====
         if (message.substring(i,i+1).equalsIgnoreCase("e"))
   =====
            count++;
   =====
      }
   =====
        System.out.println(count);
   =====
   }