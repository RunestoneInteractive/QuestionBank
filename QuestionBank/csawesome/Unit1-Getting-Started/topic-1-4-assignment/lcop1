.. activecode:: lcop1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-4-assignment
   :topics: Unit1-Getting-Started/topic-1-4-assignment
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.9945736434
   :total_students_attempting: 1290
   :num_students_correct: 1290.0
   :mean_clicks_to_correct: 1.0062015504

   Run the code below to see all the operators in action. Do all of those operators do what you expected?  What about 2 / 3? Isn't surprising that it prints 0?  See the note below.
   ~~~~
   public class Test1
   {
      public static void main(String[] args)
      {
        System.out.println(2 + 3);
        System.out.println(2 - 3);
        System.out.println(2 * 3);
        System.out.println(2 / 3);
        // == is to test while = is to assign
        System.out.println(2 == 3);
        System.out.println(2 != 3);
      }
   }
   ====
   // Test Code for Lesson 1.4 Expressions - iccv1
    import static org.junit.Assert.*;
    import org.junit.After;
    import org.junit.Before;
    import org.junit.Test;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "5\n-1\n6\n0\nfalse\ntrue";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }