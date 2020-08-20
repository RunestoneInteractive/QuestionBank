.. parsonsprob:: ch5ex2muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-9-practice-mixed-code
   :topics: Unit3-If-Statements/topic-3-9-practice-mixed-code
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :noindent: 
   :pct_on_first: 0.3069344449
   :total_students_attempting: 2639
   :num_students_correct: 2508.0
   :mean_clicks_to_correct: 3.0729665072

   The following program segment should print either "You can go out" if you don't have any homework and have cleaned and otherwise should print "You can not go out". But the blocks have been mixed up and includes <b>one extra block</b> that is not needed in a correct solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class Test1
   {
   =====
       public static void main(String[] args)
       {
   =====
           boolean homeworkLeft = false;
           boolean cleaned = true;
   =====
           if (!homeworkLeft && cleaned)
   =====
           if (homeworkLeft && cleaned) #paired
   =====
               System.out.println("You can go out");
   =====
           else
   =====
               System.out.println("You can not go out");
   =====
       }
   }