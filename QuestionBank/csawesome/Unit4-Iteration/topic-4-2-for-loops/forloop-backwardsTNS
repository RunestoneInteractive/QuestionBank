.. activecode:: forloop-backwardsTNS
   :author: Tiffani Slutsky
   :difficulty: 0.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: topic-4-2-for-loops
   :topics: Unit4-Iteration/topic-4-2-for-loops
   :from_source: F
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 3.0

   Can you make the loop count by 2s backwards? It should print out 5 3 1? Remember to change all 3 parts of the for loop.
   ~~~~
   public class ForLoop
   {
      public static void main(String[] args)
      {
        for(int count = 1; count <= 5; count++)
        {
           System.out.println(count);
        }
      }
   }
   
   ====
   import static org.junit.Assert.*;
   import org.junit.*;;
   import java.io.*;
   
   public class RunestoneTests extends CodeTestHelper
   {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "5\n3\n1";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
   }