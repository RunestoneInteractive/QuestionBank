.. activecode:: challenge3-1-primeNumbers
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-1-booleans
   :topics: Unit3-If-Statements/topic-3-1-booleans
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.0338983051
   :total_students_attempting: 236
   :num_students_correct: 164.0
   :mean_clicks_to_correct: 2.9024390244

   Experiment with the code below changing the value of number and adding more print statements with boolean expressions to determine if the numbers 5, 6, and 7 are prime. Are all odd numbers prime? Are all even numbers not prime?
   ~~~~
   public class PrimeNumbers
   {
      public static void main(String[] args)
      {
          int number = 5;
          System.out.println("A prime number is only divisible by 1 and itself.");
          System.out.println("Is " + number + " divisible by 1 up to " + number + "?");
          System.out.println("Divisible by 1? " + (number % 1 == 0));
          System.out.println("Divisible by 2? " + (number % 2 == 0));
          System.out.println("Divisible by 3? " + (number % 3 == 0));
          System.out.println("Divisible by 4? " + (number % 4 == 0));
          System.out.println("Divisible by 5? " + (number % 5 == 0));
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
       @Test
        public void testChangedCode() {
            String origCode = "public class PrimeNumbers{public static void main(String[] args){int number = 5; System.out.println(\"A prime number is only divisible by 1 and itself.\"); System.out.println(\"Is \" + number + \" divisible by 1 up to \" + number + \"?\"); System.out.println(\"Divisible by 1? \" + (number % 1 == 0)); System.out.println(\"Divisible by 2? \" + (number % 2 == 0)); System.out.println(\"Divisible by 3? \" + (number % 3 == 0)); System.out.println(\"Divisible by 4? \" + (number % 4 == 0)); System.out.println(\"Divisible by 5? \" + (number % 5 == 0));}}";
   
            boolean changed = codeChanged(origCode);
            assertTrue(changed);
        }
   
         @Test
       public void testBool6() throws IOException
       {
           String target = "number % 6 == 0";
           boolean passed = checkCodeContains("boolean check for divisibility by 6", target);
           assertTrue(passed);
       }
   
       @Test
       public void testBool7() throws IOException
       {
           String target = "number % 7 == 0";
           boolean passed = checkCodeContains("boolean check for divisibility by 7", target);
           assertTrue(passed);
       }
    }