.. activecode:: challenge2-9-random-math
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-9-Math
   :topics: Unit2-Using-Objects/topic-2-9-Math
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.1439393939
   :total_students_attempting: 132
   :num_students_correct: 78.0
   :mean_clicks_to_correct: 4.3461538462

   Complete the combination lock challenge below.
   ~~~~
   public class MathChallenge
   {
      public static void main(String[] args)
      {
          // 1. Use Math.random() to generate 3 integers from 0-40 (not including 40) and print them out.
   
   
          // 2. Calculate the number of combinations to choose 3 numbers between 0-40 (not including 40) using Math.pow() and print it out.
          // For example, Math.pow(10,2) is 10^2 and the number of permutations to choose 2 numbers between 0-9.
   
   
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
    import java.util.ArrayList;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String[] lines = output.split("\\s+");
   
            boolean passed = lines.length >= 2;
   
            passed = getResults("2+ lines of output", lines.length + " lines of output", "Expected output", passed);
            assertTrue(passed);
        }
   
        @Test
        public void test2()
        {
            String output = getMethodOutput("main");
            boolean passed = output.contains("64000");
            passed = getResults("true", "" + passed, "Prints 40^3", passed);
            assertTrue(passed);
        }
   
        @Test
        public void test3()
        {
            String code = getCode();
            int num = countOccurences(code, "(int)(Math.random()*40");
   
            boolean passed = num >= 3;
            passed = getResults("3", ""+num, "Calls to Math.random() for a random number from 0 up to 40", passed);
            assertTrue(passed);
        }
   
        @Test
        public void test4()
        {
            String code = getCode();
            int num = countOccurences(code, "Math.pow(");
   
            boolean passed = num >= 1;
            passed = getResults("1 or more", ""+num, "Calls to Math.pow(...)", passed);
            assertTrue(passed);
        }
    }