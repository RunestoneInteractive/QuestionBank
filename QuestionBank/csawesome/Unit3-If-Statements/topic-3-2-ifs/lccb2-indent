.. activecode:: lccb2-indent
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-2-ifs
   :topics: Unit3-If-Statements/topic-3-2-ifs
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.1587301587
   :total_students_attempting: 126
   :num_students_correct: 89.0
   :mean_clicks_to_correct: 4.0898876404

   The code below doesn't work as expected.  Fix it to only print ``Wear a coat`` and ``Wear gloves`` when isCold is true.
   ~~~~
   public class Test1
   {
      public static void main(String[] args)
      {
          boolean isCold = false;
          if (isCold = true);
              System.out.println("Wear a coat");
              System.out.println("Wear gloves");
   
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
            String expect = "";
            boolean passed = getResults(expect, output, "Expected output from main if isCold is false");
            assertTrue(passed);
        }
        @Test
        public void testCountCurlies()
        {
            String code = getCode();
            int num = countOccurences(code, "{");
            boolean passed = num >= 3;
   
            getResults("3", "" + num, "Number of {", passed);
            assertTrue(passed);
        }
    }