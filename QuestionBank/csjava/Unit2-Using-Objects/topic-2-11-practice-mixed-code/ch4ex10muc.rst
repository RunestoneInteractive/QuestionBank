.. parsonsprob:: ch4ex10muc
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

   The main method in the following class should print the part of the message starting with the word "nice".  But, the blocks have been mixed up and include an extra block that isn't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
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
           int pos = message.indexOf("nice");
   =====
           System.out.println(message.substring(pos));
   =====
       }
   =====
   }
   =====
           int pos = message.indexof("nice"); #distractor