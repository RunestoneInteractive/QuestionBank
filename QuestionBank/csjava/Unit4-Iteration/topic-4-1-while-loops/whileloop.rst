.. activecode:: whileloop
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit4-Iteration
   :subchapter: topic-4-1-while-loops
   :topics: Unit4-Iteration/topic-4-1-while-loops
   :from_source: F
   :language: java
   :autograde: unittest
   :practice: T

   Here is a while loop that counts from 1 to 5 that demonstrates the 3 steps of writing a loop. Can you change it to count from 2 to 10?
   ~~~~
   public class LoopTest1
   {
      public static void main(String[] args)
      {
        // 1. initialize the loop variable
        int count = 1;

        // 2. test the loop variable
        while (count <= 5)
        {
           System.out.println(count);
           // 3. change the loop variable
           count++;
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