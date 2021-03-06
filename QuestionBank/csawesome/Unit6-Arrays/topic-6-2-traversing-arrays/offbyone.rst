.. activecode:: offbyone
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: topic-6-2-traversing-arrays
   :topics: Unit6-Arrays/topic-6-2-traversing-arrays
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.4666666667
   :total_students_attempting: 120
   :num_students_correct: 102.0
   :mean_clicks_to_correct: 1.931372549

   The following code has an ArrayIndexOutOfBoundsException. It has 2 common off-by-one errors in the loop. Can you fix it and make the loop print out all the scores?
   ~~~~
   public class OffByone
   {
      public static void main(String[] args)
      {
          int[] scores = { 10, 9, 8, 7};
          // Make this loop print out all the scores!
          for (int i = 1; i <= scores.length; i++)
          {
               System.out.println(  scores[i] );
          }
      }
    }
    ====
    // Test for Lesson 6.2 OffByOne
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("OffByone");
        }
   
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "9\n8\n7".replaceAll(" ", "\n");
   
            boolean passed = output.contains(expect);
            getResults(expect, output, "Testing right off-by-one error", passed);
            assertTrue(passed);
        }
   
        @Test
        public void test2()
        {
            String output = getMethodOutput("main");
            String expect = "10\n9\n8".replaceAll(" ", "\n");
   
            boolean passed = output.contains(expect);
            getResults(expect, output, "Testing left off-by-one error", passed);
            assertTrue(passed);
        }
        @Test
        public void checkCodeContains1(){
            boolean passed = checkCodeContains("fixes to for loop", "for (int i = 0; i <");
            assertTrue(passed);
        }
    }