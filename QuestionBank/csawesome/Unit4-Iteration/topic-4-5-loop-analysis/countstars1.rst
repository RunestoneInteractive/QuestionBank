.. activecode::  countstars1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: topic-4-5-loop-analysis
   :topics: Unit4-Iteration/topic-4-5-loop-analysis
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 138
   :num_students_correct: 138.0
   :mean_clicks_to_correct: 1.0

   How many stars are printed out in this loop? How many times does the loop run? Figure it out on paper before you run the code.
   ~~~~
   public class CountLoop
   {
   
      public static void main(String[] args)
      {
          for (int i = 3; i < 7; i++)
               System.out.print("*");
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
      @Test
      public void testMain() throws IOException
      {
        String output = getMethodOutput("main");
        String expect = "****\n";
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
    }