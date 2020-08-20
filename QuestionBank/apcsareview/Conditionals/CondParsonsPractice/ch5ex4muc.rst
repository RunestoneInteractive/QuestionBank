.. parsonsprob:: ch5ex4muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Conditionals
   :subchapter: CondParsonsPractice
   :topics: Conditionals/CondParsonsPractice
   :from_source: T
   :numbered: left
   :adaptive:
   :noindent:

   The main method in the following class should print out if a string has the word "bomb" in it or not. But, the blocks have been mixed up and includes <b>an extra block</b> that isn't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class Test1
   {
   =====
       public static void main(String[] args)
       {
   =====
          String message = "Place the bomb today";
   =====
          if (message.indexOf(" bomb ") >= 0)
   =====
          if (message.indexof(" bomb ") >= 0) #paired
   =====
              System.out.println("Possible bomb threat");
   =====
          else
   =====
              System.out.println("No mention of bomb");
   =====
       }
   }