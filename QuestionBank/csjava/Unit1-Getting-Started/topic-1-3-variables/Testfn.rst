.. activecode:: Testfn
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-3-variables
   :topics: Unit1-Getting-Started/topic-1-3-variables
   :from_source: F
   :language: java
   :autograde: unittest

   Try the following code and notice the syntax error when we try to change the constant PI. Put the comment symbols // in front of that line to remove the error and run it again.
   ~~~~
   public class TestFinal
   {
      public static void main(String[] args)
      {
        final double PI = 3.14;
        System.out.println(PI);
        PI = 4.2; // This will cause a syntax error
      }
   }
   ====
   // should pass if/when they run code
   import static org.junit.Assert.*;
   import org.junit.*;;
   import java.io.*;

   public class RunestoneTests extends CodeTestHelper
   {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "3.14";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
   }