.. parsonsprob:: 5_9_van_Mierlo
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

   The main method in the following class should print if your name starts with a vowel or not. But, the blocks have been mixed up.  Drag the blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class Test1
   {
   =====
       public static void main(String[] args)
       {
   =====
           String name = "Julian";
           String firstLetter = name.substring(0,1);
           String lowerFirst = firstLetter.toLowerCase();
   =====
           boolean aF = lowerFirst.equals("a");
           boolean eF = lowerFirst.equals("e");
           boolean iF = lowerFirst.equals("i");
           boolean oF = lowerFirst.equals("o");
           boolean uF = lowerFirst.equals("u");

   =====
           if (aF || eF || iF || oF || uF)
           {
   =====
               System.out.println("Starts with a vowel");
           }
   =====
           else
           {
   =====
               System.out.println("Starts with a consonant");
           }
   =====
       }
   }