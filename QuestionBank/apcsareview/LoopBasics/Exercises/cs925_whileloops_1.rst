.. activecode:: cs925_whileloops_1
   :author: Doug Vermes
   :difficulty: 0.0
   :basecourse: apcsareview
   :chapter: LoopBasics
   :subchapter: Exercises
   :topics: LoopBasics/Exercises
   :from_source: F
   :above:
   :language: java

   Write a method to print to the terminal window the multiples of 3 from 3 to x 
   inclusive.
   ~~~~
   public class WhileLoops
   {
      public static void multiplesOfThree(int x)
      {
           // your code goes here. In this method, we will print the result
           // NOT return it.
   
      }
   
      // DO NOT CHANGE ANYTHING BELOW THIS LINE
      public static void main(String[] args)
      {
          System.out.println("multiplesOfThree(3)  should print: 3");
          System.out.print("Your program output: ");
          System.out.println();
          multiplesOfThree(3);
   
          System.out.println("--------------------------------------------------------");
          System.out.println("multiplesOfThree(12) should print: 3 6 9 12");
          System.out.print("Your program output: ");
          System.out.println();
          multiplesOfThree(12);
   
          System.out.println("--------------------------------------------------------");
          System.out.println("multiplesOfThree(17) should print: 3 6 9 12 15");
          System.out.print("Your program output: ");
          System.out.println();
          multiplesOfThree(17);
      }
   }
   ====