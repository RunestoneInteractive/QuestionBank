.. activecode:: lccv1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-4-assignment
   :topics: Unit1-Getting-Started/topic-1-4-assignment
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.9955156951
   :total_students_attempting: 1338
   :num_students_correct: 1338.0
   :mean_clicks_to_correct: 1.0044843049

   Try the code below to see how score is incremented by 1. Try substituting 2 instead of 1 to see what happens.
   ~~~~
   public class Test1
   {
      public static void main(String[] args)
      {
        int score = 0;
        System.out.println(score);
        score = score + 1;
        System.out.println(score);
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
            String expect = "0\n1\n";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }