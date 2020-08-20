.. activecode:: code1_6_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-6-casting
   :topics: Unit1-Getting-Started/topic-1-6-casting
   :from_source: T
   :language: java
   :autograde: unittest

   Try the code below to see two integer overflow errors for a positive and negative number. An int cannot hold that many digits! Fix the integer overflow error by deleting the last 0 in the numbers.
   ~~~~
   public class TestOverflow
   {
      public static void main(String[] args)
      {
        int id = 2147483650; // overflow error!
        int negative = -2147483650; // overflow
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
            String expect = "214748365\n-214748365\n";

            boolean passed = getResults(expect, output, "Fixed Integer Overflow Error", true);
            assertTrue(passed);
        }
    }