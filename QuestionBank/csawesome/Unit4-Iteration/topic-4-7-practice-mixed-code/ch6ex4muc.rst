.. parsonsprob:: ch6ex4muc
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
   :pct_on_first: 0.7934834691
   :total_students_attempting: 2087
   :num_students_correct: 2018.0
   :mean_clicks_to_correct: 1.2789890981

   The main method in the following class should print out the values from 0 to 100 by 20's (0, 20, 40, .. 100). But, the blocks have been mixed up and include <b>an extra block</b> that isn't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class Test1
   {
   =====
       public static void main(String[] args)
       {
   =====
          for (int i = 0; i <= 100; i+=20)
   =====
          for (int i = 100; i >= 0; i-=20) #paired
   =====
              System.out.println(i);
   =====
       }
   =====
   }