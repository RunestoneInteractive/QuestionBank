.. activecode:: lcct1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-6-casting
   :topics: Unit1-Getting-Started/topic-1-6-casting
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.9945770065
   :total_students_attempting: 922
   :num_students_correct: 920.0
   :mean_clicks_to_correct: 1.0032608696

   What happens when you divide an int by an int or with a double operand or with the type cast (double) on one of the operands?
   ~~~~
   public class OperatorTest
   {
      public static void main(String[] args)
      {
        System.out.println(1 / 3);
        System.out.println(1.0 / 3);
        System.out.println(1 / 3.0);
        System.out.println((double) 1 / 3);
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
            String expect = "0\n0.3333333333333333\n0.3333333333333333\n0.3333333333333333\n";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
    }