.. parsonsprob:: ch3ex5muc
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit1-Getting-Started/topic-1-8-practice-mixed-code
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:
   :noindent:

   The main method in the following class should calculate the number of months it would take you to save 500 if you make 50 a week. But, the blocks have been mixed up and may include an extra block that isn't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class Test1
   {
   =====
       public static void main(String[] args)
       {
   =====
           double weeklyRate = 50;
           double goal = 500;
   =====
           double numWeeks = goal / weeklyRate;
   =====
           double numMonths = numWeeks / 4;
   =====
           System.out.println(numMonths);
   =====
       } // end main method
   } // end class
   =====
       public void main(String[] args)
       { #distractor