.. activecode:: code1_6_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-6-casting
   :topics: Unit1-Getting-Started/topic-1-6-casting
   :from_source: T
   :language: java
   :autograde: unittest

   Run the code below to see how a decimal number can be formatted to show 2 digits after the decimal point.
   ~~~~
   public class TestFormat
   {
      public static void main(String[] args)
      {
        double number = 10 / 3.0;
        System.out.println(number);
        System.out.println( String.format("%.02f", number) );
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "3.0\n3.00\n";

            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }