.. activecode:: lcct1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-6-casting
   :topics: Unit1-Getting-Started/topic-1-6-casting
   :from_source: F
   :language: java

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
        System.out.println((double) (1 / 3));
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