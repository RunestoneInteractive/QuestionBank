.. parsonsprob:: ch6ex5muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: topic-4-7-practice-mixed-code
   :topics: Unit4-Iteration/topic-4-7-practice-mixed-code
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :noindent: 
   :pct_on_first: 0.749034749
   :total_students_attempting: 2072
   :num_students_correct: 2005.0
   :mean_clicks_to_correct: 1.3226932668

   The main method in the following class should print out the values from 100 to 0 by 10's (100, 90, 80, ... 0). But, the blocks have been mixed up and include <b>an extra block</b> that is not needed in a correct solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class Test1
   {
   =====
       public static void main(String[] args)
       {
   =====
           for (int i = 100; i >= 0; i -= 10)
   =====
           for (int i = 0; i <= 100; i += 10) #paired
   =====
               System.out.println(i);
   =====
       }
   =====
   }