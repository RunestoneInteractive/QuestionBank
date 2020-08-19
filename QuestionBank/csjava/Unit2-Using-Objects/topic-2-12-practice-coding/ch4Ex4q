.. activecode::  ch4Ex4q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-12-practice-coding
   :topics: Unit2-Using-Objects/topic-2-12-practice-coding
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T

   The following code should print the first 3 letters of the string ``message`` all in lowercase letters. However, the code has errors.  Fix the errors so that the code runs as intended.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           String message = "Meet me by the bridge":
           String part = message.substring(1,3);
           String lower = message.toLowerCase();
           System.println(lower);
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
             String expect = "mee";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
           @Test
         public void testCodeContains()
         {
             String target = ".substring(0,3)";
             boolean passed = checkCodeContains("substring method fixed", target);
             assertTrue(passed);
         }
     }