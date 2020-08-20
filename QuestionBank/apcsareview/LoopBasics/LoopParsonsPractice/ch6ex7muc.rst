.. parsonsprob:: ch6ex7muc
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

   The main method in the following class should print 3 rows with 6 <code>*</code> in each row.  But, the blocks have been mixed up and include <b>two extra blocks</b> that aren't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class Test1
   {
   =====
       public static void main(String[] args)
       {
   =====
           for (int x = 3; x > 0; x--) {
   =====
           for (int x = 0; x <= 3; x++) { #paired
   =====
               for (int y = 6; y > 0; y--) {
   =====
               for (int y = 0; y <= 6; y++) { #paired
   =====
                   System.out.println("*");
   =====
               }
           }
       }
   }