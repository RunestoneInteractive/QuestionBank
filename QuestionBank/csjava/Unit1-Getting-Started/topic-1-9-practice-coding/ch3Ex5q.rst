.. activecode::  ch3Ex5q
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit1-Getting-Started/topic-1-9-practice-coding
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T

   The following code should calculate the number of whole days in 320893 seconds. However, the code has errors.  Fix the code so that it compiles and runs correctly.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           int numSecs = 320893;
           int numHours = numSecs   3600;
           int numDays = numHours   24;
           System.out.println numDays);

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
             String expect = "3\n";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
     }