.. activecode::  ch6ex11nq
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit4-Iteration
   :subchapter: topic-4-8-practice-coding
   :topics: Unit4-Iteration/topic-4-8-practice-coding
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T

   Finish the code below to print the values for ``10 * x`` where ``x`` changes from 0 to 10 using a loop.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {

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
             String expect = "0\n10\n20\n30\n40\n50\n60\n70\n80\n90\n100\n";

             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
          @Test
         public void testForLoop()
         {
            // String target = "for (";
            // boolean passed = checkCodeContains("for loop", target);
            String code = getCode();
            boolean passed = code.contains("for") || code.contains("while");
            getResults("Expected loop",""+passed, "Checking for loop",passed);
            assertTrue(passed);
         }
     }