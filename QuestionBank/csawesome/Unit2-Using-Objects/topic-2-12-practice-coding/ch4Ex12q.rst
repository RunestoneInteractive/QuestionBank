.. activecode::  ch4Ex12q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-12-practice-coding
   :topics: Unit2-Using-Objects/topic-2-12-practice-coding
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.5737704918
   :total_students_attempting: 61
   :num_students_correct: 51.0
   :mean_clicks_to_correct: 1.568627451

   The following code should replace ``lol`` in the message with ``laugh out loud`` and print the new message using indexOf and substring.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           String message = "That was great - lol.";
   
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
             String expect = "That was great - laugh out loud";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
   
          @Test
         public void testCodeContains()
         {
             String target = ".substring(";
             boolean passed = checkCodeContains("substring method", target);
             assertTrue(passed);
         }
          @Test
         public void testCodeContains2()
         {
             String target = ".indexOf(";
             boolean passed = checkCodeContains("indexOf method", target);
             assertTrue(passed);
         }
     }