.. parsonsprob:: 5_Mixed_2_van_Mierlo
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

   The following program segment should print either "You can go out" if you don't have any homework and have cleaned and otherwise should print "You can not go out". But the blocks have been mixed up and includes <b>one extra block</b> that is not needed in a correct solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class Test1
   {
   =====
       public static void main(String[] args)
       {
   =====
           boolean homework = false;
           boolean cleaned = true;
   =====
           if (!homework && cleaned)
           {
   =====
           if (homework && cleaned) 
           { #paired
   =====
               System.out.println("You can go out");
           }
   =====
           else
           {
   =====
               System.out.println("You can not go out");
           }
   =====
       }
   }