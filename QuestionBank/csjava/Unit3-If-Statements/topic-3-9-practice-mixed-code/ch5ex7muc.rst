.. parsonsprob:: ch5ex7muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-9-practice-mixed-code
   :topics: Unit3-If-Statements/topic-3-9-practice-mixed-code
   :from_source: F
   :numbered: left
   :practice: T
   :adaptive:
   :noindent:

   The main method in the following class should print the alarm time.  If it is a weekday you should get up at 7:00am and if not get up at 10:00am. But, the blocks have been mixed up.  Drag the needed blocks from the left and put them in the correct order on the right.

   -----
   public class Test1
   {
   =====
       public static void main(String[] args)
       {
   =====
           boolean weekend = false;
   =====
           if (!weekend)
   =====
               System.out.println("7:00am");
   =====
           else
   =====
               System.out.println("10:00am");
   =====
       }
   }