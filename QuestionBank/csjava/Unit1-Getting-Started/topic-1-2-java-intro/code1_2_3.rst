.. activecode:: code1_2_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-2-java-intro
   :topics: Unit1-Getting-Started/topic-1-2-java-intro
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T

   Fix the code below.
   ~~~~
   public class Error1
   {
      public static void main(String[] args)
      {
         System.out.println("Hi there!);
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
            String expect = "Hi there!";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
   }