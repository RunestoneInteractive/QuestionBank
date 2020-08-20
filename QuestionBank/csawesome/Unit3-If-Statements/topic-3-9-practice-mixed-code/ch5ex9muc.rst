.. parsonsprob:: ch5ex9muc
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
   :pct_on_first: 0.6506819182
   :total_students_attempting: 2273
   :num_students_correct: 2124.0
   :mean_clicks_to_correct: 1.6473634652

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
   =====
               System.out.println("Starts with a vowel");
   =====
           else
   =====
               System.out.println("Starts with a consonant");
   =====
       }
   }