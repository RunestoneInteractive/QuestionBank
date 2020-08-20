.. parsonsprob:: ch6ex6muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: LoopBasics
   :subchapter: LoopParsonsPractice
   :topics: LoopBasics/LoopParsonsPractice
   :from_source: T
   :numbered: left
   :adaptive:
   :noindent:

   The main method in the following class should print 10 rows with 5 <code>*</code> in each row.   But, the blocks have been mixed up and include <b>one extra block</b> that isn't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class Test1
   {
       public static void main(String[] args)
       {
   =====
           for (int x = 0; x < 10; x++) {
   =====
               for (int y = 0; y < 5; y++) {
   =====
               for (int y = 0; y <= 5; y++) { #paired
   =====
                   System.out.println("*");
   =====
               }
   =====
           }
   =====
       }
   }