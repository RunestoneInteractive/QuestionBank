.. activecode:: lccbElseIf
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-4-else-ifs
   :topics: Unit3-If-Statements/topic-3-4-else-ifs
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.0599250936
   :total_students_attempting: 267
   :num_students_correct: 249.0
   :mean_clicks_to_correct: 1.9879518072

   Run the code below and try changing the value of x to get each of the three possible lines in the conditional to print.
   ~~~~
   public class TestElseIf
   {
      public static void main(String[] args)
      {
        int x = 2;
        if (x < 0)
        {
          System.out.println("x is negative");
        }
        else if (x == 0)
        {
           System.out.println("x is 0");
        }
        else
        {
          System.out.println("x is positive");
        }
        System.out.println("after conditional");
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testChangedCode() {
            String origCode = "public class TestElseIf { public static void main(String[] args) { int x = 2; if (x < 0) { System.out.println(\"x is negative\");  } else if (x == 0) {  System.out.println(\"x is 0\"); } else { System.out.println(\"x is positive\"); } System.out.println(\"after conditional\"); } }";
            boolean changed = codeChanged(origCode);
            assertTrue(changed);
        }
    }