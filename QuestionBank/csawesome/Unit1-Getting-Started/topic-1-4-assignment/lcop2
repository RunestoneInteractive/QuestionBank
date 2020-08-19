.. activecode:: lcop2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-4-assignment
   :topics: Unit1-Getting-Started/topic-1-4-assignment
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.9951923077
   :total_students_attempting: 1248
   :num_students_correct: 1248.0
   :mean_clicks_to_correct: 1.0056089744

   In the example below, try to guess what it will print out and then run it to see if you are right.
   ~~~~
   public class Test1
   {
      public static void main(String[] args)
      {
        System.out.println(11 % 10);
        System.out.println(3 % 4);
        System.out.println(8 % 2);
        System.out.println(9 % 2);
      }
   }
   ====
   // Test Code for Lesson 1.4 Expressions - lcop2
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
            String expect = "1\n3\n0\n1";
            boolean passed = getResults(expect, output, "Expected output from main",true);
            assertTrue(passed);
        }
    }