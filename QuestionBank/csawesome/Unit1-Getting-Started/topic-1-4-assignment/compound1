.. activecode:: compound1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-4-assignment
   :topics: Unit1-Getting-Started/topic-1-4-assignment
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.9975020816
   :total_students_attempting: 1201
   :num_students_correct: 1201.0
   :mean_clicks_to_correct: 1.0024979184

   In the example below, try to guess what it will print out and then run it to see if you are right. Remember to consider **operator precedence**. How do the parentheses change the precedence?
   ~~~~
   public class TestCompound
   {
      public static void main(String[] args)
      {
        System.out.println(2 + 3 * 2);
        System.out.println((2 + 3) * 2);
        System.out.println(2 + (3 * 2));
      }
   }
   ====
   // Test Code for Lesson 1.4 Expressions - compounds
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
            String expect = "8\n10\n8";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }