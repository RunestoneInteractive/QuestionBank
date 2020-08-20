.. parsonsprob:: ch6ex5muc
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

   The main method in the following class should print out the values from 100 to 0 by 10's (100, 90, 80, ... 0). But, the blocks have been mixed up and include <b>an extra block</b> that is not needed in a correct solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class Test1
   {
   =====
       public static void main(String[] args)
       {
   =====
           for (int i = 100; i >= 0; i--)
   =====
           for (int i = 0; i <= 100; i++) #paired
   =====
               System.out.println(i);
   =====
       }
   =====
   }