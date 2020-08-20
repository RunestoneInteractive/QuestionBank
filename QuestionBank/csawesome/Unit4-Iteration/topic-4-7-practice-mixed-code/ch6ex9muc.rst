.. parsonsprob:: ch6ex9muc
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
   :pct_on_first: 0.3947368421
   :total_students_attempting: 1938
   :num_students_correct: 1828.0
   :mean_clicks_to_correct: 3.1170678337

   The main method in the following class should print 11111, 22222, 33333, 44444, and 55555. But, the blocks have been mixed up and contain <b>two extra blocks</b> that are not needed in a correct solution.  Drag the blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class Test1
   {
   =====
       public static void main(String[] args)
       {
   =====
           for (int x = 1; x <= 5; x++) {
   =====
           for (int x = 1; x < 5; x++) { #paired
   =====
               for (int y = 0; y < 5; y++) {
   =====
                   System.out.print(x);
   =====
                   System.out.print(y); #paired
   =====
               } //end inner loop
               System.out.println();
   =====
           } //end outer loop
   =====
       }
   }