.. activecode::  ch4Ex8q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-9-practice-coding
   :topics: Unit1-Getting-Started/topic-1-9-practice-coding
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.6754385965
   :total_students_attempting: 342
   :num_students_correct: 301.0
   :mean_clicks_to_correct: 1.6079734219

   Finish the code below to print your favorite animal and food.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           String animal =
           String food =
           System.out.println();
   
       }
   }
   ====
   import static org.junit.Assert.*;
     import org.junit.*;;
     import java.io.*;
   
     public class RunestoneTests extends CodeTestHelper
     {
        @Test
         public void testPrintStringsA() throws IOException
         {
           String target1 = "+animal";
           boolean passed1 = checkCodeContains("print animal string", target1);
           assertTrue(passed1);
         }
   
          @Test
         public void testPrintStringsB() throws IOException
         {
             String target1 = "+food";
             boolean passed1 = checkCodeContains("print food string", target1);
             assertTrue(passed1);
         }
     }