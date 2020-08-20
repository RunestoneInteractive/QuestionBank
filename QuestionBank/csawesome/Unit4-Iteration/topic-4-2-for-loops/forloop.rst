.. activecode:: forloop
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: topic-4-2-for-loops
   :topics: Unit4-Iteration/topic-4-2-for-loops
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.5473684211
   :total_students_attempting: 285
   :num_students_correct: 272.0
   :mean_clicks_to_correct: 1.5514705882

   Here is a for loop that counts from 1 to 5. Can you change it to count from 2 to 10?
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
            String expect = "2\n3\n4\n5\n6\n7\n8\n9\n10\n";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
   }