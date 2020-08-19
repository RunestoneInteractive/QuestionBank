.. activecode:: lcsm1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-7-string-methods
   :topics: Unit2-Using-Objects/topic-2-7-string-methods
   :from_source: F
   :language: java
   :autograde: unittest

   This code shows the output from String methods length, substring, and indexOf. How many letters does substring(0,3) return? What does indexOf return when its argument is not found?
   ~~~~
   public class Test1
   {
      public static void main(String[] args)
      {
        String message1 = "This is a test";
        String message2 = "Hello Class";

        System.out.println(message1.length());
        System.out.println(message2.length());

        System.out.println(message1.substring(0,3));
        System.out.println(message2.substring(4,5));
        System.out.println(message1.substring(5));

        System.out.println(message1.indexOf("is")); // This will match the is in "This"!
        System.out.println(message1.indexOf("Hello"));
        System.out.println(message2.indexOf("Hello"));

        System.out.println(message2.toLowerCase());
        System.out.println(message2.toUpperCase());
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
            String expect = "14\n11\nThi\no\nis a test\n2\n-1\n0\nhello class\nHELLO CLASS";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }