.. parsonsprob:: ch4ex9muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-11-practice-mixed-code
   :topics: Unit2-Using-Objects/topic-2-11-practice-mixed-code
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :noindent: 
   :pct_on_first: 0.3742653882
   :total_students_attempting: 3233
   :num_students_correct: 3107.0
   :mean_clicks_to_correct: 2.4962986804

   The main method in the following class should print the first 3 letters of message in uppercase letters. But, the blocks have been mixed up and include an extra block that isn't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class Test1
   {
   =====
       public static void main(String[] args)
   =====
       {
   =====
           String message = "Have a nice day!";
   =====
           String part = message.substring(0,3);
   =====
           String upper = part.toUpperCase();
   =====
           System.out.println(upper);
   =====
       }
   =====
   }
   =====
           String part = message.substring(0,4); #distractor