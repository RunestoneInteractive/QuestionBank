.. activecode:: random1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-9-Math
   :topics: Unit2-Using-Objects/topic-2-9-Math
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.9968152866
   :total_students_attempting: 314
   :num_students_correct: 314.0
   :mean_clicks_to_correct: 1.0031847134

   Try out the following code.  Run it several times to see what it prints each time.
   ~~~~
   public class Test3
   {
      public static void main(String[] args)
      {
        System.out.println(Math.random());
        System.out.println(Math.random());
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
            String expect = output;
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }