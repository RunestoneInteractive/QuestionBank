.. activecode:: whileloopbugs
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: topic-4-1-while-loops
   :topics: Unit4-Iteration/topic-4-1-while-loops
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.4207650273
   :total_students_attempting: 183
   :num_students_correct: 169.0
   :mean_clicks_to_correct: 2.1715976331

   The while loop should print out the numbers 1 to 8, but it has 2 errors that cause an infinite loop and an off-by-one error. Can you fix the errors? If you run an infinite loop, you may need to refresh the page to stop it (so make sure all active code windows on the page have been saved and click on Load History after refreshing).
   ~~~~
   public class LoopTest2
   {
      public static void main(String[] args)
      {
        int count = 1;
        while (count < 8)
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
        public RunestoneTests() {
            super("LoopTest2");
        }
   
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "1\n2\n3\n4\n5\n6\n7\n8";
   
            boolean passed = getResults(expect, output, "Running main");
            assertTrue(passed);
        }
    }