.. parsonsprob:: 5_Mixed_3_van_Mierlo
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

   The main method in the following class should print if x is in the range of 1 to 10 (inclusive) or not. But, the blocks have been mixed up and includes <b>an extra block</b> that isn't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class Test1
   {
   =====
       public static void main(String[] args)
       {
   =====
           int x = 3;
   =====
           if (x >= 1 && x <= 10)
           {
   =====
           if (x >= 1 || x <= 10) 
           { #paired
   =====
               System.out.println("1 <= x <= 10");
           }
   =====
           else
           {
   =====
               System.out.println("x is not in range");
           }
   =====
       }
   }