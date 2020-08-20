.. parsonsprob:: removeA
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: LoopBasics
   :subchapter: lWhile
   :topics: LoopBasics/lWhile
   :from_source: T
   :numbered: left
   :adaptive:
   :noindent:

   The following method has the correct code to return a string with all a's removed, but the code is mixed up.  Drag the blocks from the left area into the correct order in the right area.  Click on the "Check Me" button to check your solution.
   -----
   public static String remA(String s)
   {
   =====
      int index = 0;
   =====
      // while still an a in str
      while (s.indexOf("a") >= 0)
      {
         index = s.indexOf("a");
         s = s.substring(0,index) +
             s.substring(index+1);
      }
   =====
      return s;
   =====
   } // end method