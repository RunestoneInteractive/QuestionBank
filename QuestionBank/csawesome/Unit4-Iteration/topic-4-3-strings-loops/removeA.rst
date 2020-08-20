.. parsonsprob:: removeA
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: topic-4-3-strings-loops
   :topics: Unit4-Iteration/topic-4-3-strings-loops
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :noindent: 
   :pct_on_first: 0.2815588817
   :total_students_attempting: 3541
   :num_students_correct: 3362.0
   :mean_clicks_to_correct: 3.8542534206

   The following program removes all the a's from a string, but the code is mixed up.  Drag the blocks from the left area into the correct order in the right area.  Click on the "Check Me" button to check your solution.
   -----
   public static void main(String[] args)
   {
   =====
      String s = "are apples tasty without an a?";
      int index = 0;
      System.out.println("Original string: " + s);
   =====
      // while there is an a in s
      while (s.indexOf("a") >= 0)
      {
   =====
         // Find the next index for an a
         index = s.indexOf("a");
   =====
         // Remove the a at index by concatenating
         // substring up to index and then rest of the string.
         s = s.substring(0,index) +
             s.substring(index+1);
   =====
      } // end loop
   =====
      System.out.println("String with a's removed:" + s);
   =====
   } // end method