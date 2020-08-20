.. activecode:: challenge1-2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-2-java-intro
   :topics: Unit1-Getting-Started/topic-1-2-java-intro
   :from_source: F
   :language: java
   :autograde: unittest
   :practice: T

   Fix the code below.
   ~~~~
   public class Challenge1_2
   {
      public static void main(String[] args)
      {
         System.out.print("Good morning! ")
         system.out.print("Good afternoon!);
         System.Print " And good evening!";
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
            String expect = "Good morning! Good afternoon! And good evening";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
   }