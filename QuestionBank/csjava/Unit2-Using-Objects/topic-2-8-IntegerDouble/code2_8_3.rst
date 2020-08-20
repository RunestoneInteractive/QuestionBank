.. activecode:: code2_8_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-8-IntegerDouble
   :topics: Unit2-Using-Objects/topic-2-8-IntegerDouble
   :from_source: T
   :language: java
   :autograde: unittest

   Find and fix the bugs below to use the correct Integer and Double methods and variables.
   ~~~~
   public class Debug
   {
      public static void main(String[] args)
      {
        integer i = 2.3;
        Double d = 5;
        System.out.println( i.intValue );
        System.out.println( doubleValue() );
        // Print out the min and max values possible for integers
        System.out.println(Integer.min_value);
        System.out.println( i.MAX_VALUE() );
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
            String expect = "2\n5.0\n-2147483648\n2147483647";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
        @Test
        public void testCode() throws IOException
        {
           String target = "Integer.MAX_VALUE";
           boolean passed = checkCodeContains("MAX_VALUE", target);
           assertTrue(passed);
        }
    }