.. parsonsprob:: ch3ex3muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-11-practice-mixed-code
   :topics: Unit2-Using-Objects/topic-2-11-practice-mixed-code
   :from_source: F
   :numbered: left
   :practice: T
   :adaptive:
   :noindent:

   The main method in the following class should print a random number from 1 to 50. But, the blocks have been mixed up and may include an extra block that isn't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class Test1
   {
   =====
       public static void main(String[] args)
       {
   =====
           int num = (int)(Math.random() * 50) + 1;
   =====
           System.out.println(num);
   =====
       } // end main method

   =====
   } // end of class
   =====
           int num = Math.random() * 50; #distractor