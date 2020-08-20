.. activecode:: forloopfromwhile
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
   :pct_on_first: 0.1230769231
   :total_students_attempting: 260
   :num_students_correct: 198.0
   :mean_clicks_to_correct: 2.4393939394

   Here is a while loop that counts from 5 to 10. Run it and see what it does. Can you change it to a for-loop? Run your for-loop. Does it do the same thing?
   ~~~~
   public class ForLoopFromWhile
   {
      public static void main(String[] args)
      {
        int count = 5;
        while (count <= 10)
        {
           System.out.println(count);
           count++;
        }
      }
   }
   ====
   // Test Code for Lesson 4.1 - For Loop
   
    import static org.junit.Assert.*;
   
    import org.junit.After;
    import org.junit.Before;
    import org.junit.Test;
   
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("ForLoopFromWhile");
        }
   
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "5\n6\n7\n8\n9\n10\n";
   
            boolean passed = getResults(expect, output, "Running main");
            assertTrue(passed);
        }
   
        @Test
        public void testWhile() throws IOException
        {
            String target = "while (*)";
            boolean passed = checkCodeNotContainsRegex("while loop", target);
            assertTrue(passed);
        }
   
        @Test
        public void testFor() throws IOException
        {
            String target = "for (int * = #; * ? #; *~)";
            boolean passed = checkCodeContainsRegex("for loop", target);
            assertTrue(passed);
        }
    }