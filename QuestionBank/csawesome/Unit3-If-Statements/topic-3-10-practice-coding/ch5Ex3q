.. activecode::  ch5Ex3q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-10-practice-coding
   :topics: Unit3-If-Statements/topic-3-10-practice-coding
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.625
   :total_students_attempting: 56
   :num_students_correct: 56.0
   :mean_clicks_to_correct: 1.4285714286

   The following code should print "You can go out" if you have done your homework and cleaned your room. However, the code has errors.  Fix the code so that it compiles and runs correctly.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           boolean doneHomework = True;
           boolean cleanedRoom = true;
           if (doneHomework && cleanedRoom)
                System.out.println("You cannot go out");
           else
               System.out.println("You can go out");
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
             String expect = "You can go out\n";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
     }