.. activecode::  ch4Ex10q
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
   :pct_on_first: 0.6166666667
   :total_students_attempting: 60
   :num_students_correct: 57.0
   :mean_clicks_to_correct: 1.8421052632

   The following code starts with ``String firstNameCaps = ALEX;`` and should print ``Alex``.  Use the ``toLowerCase`` and ``substring`` methods to do accomplish this task.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           String name1 = "ALEX";
   
   
   
           System.out.println(firstNameCaps);
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
             String expect = "Alex";
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
     }