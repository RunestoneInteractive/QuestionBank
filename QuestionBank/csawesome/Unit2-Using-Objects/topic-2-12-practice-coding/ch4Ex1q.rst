.. activecode::  ch4Ex1q
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
   :pct_on_first: 0.9666666667
   :total_students_attempting: 60
   :num_students_correct: 60.0
   :mean_clicks_to_correct: 1.0333333333

   The following code should get the first letter of the first name, middle name, and last name and append (concatenate) them together and then return them all in lowercase.  However, the code has errors.  Fix the code so that it compiles and runs correctly.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           String firstName = "Sofia';
           String middleName = "Maria";
           String lastName  "Hernandez";
           String initials = firstname.substring(0,1) +
                             middleName.subString(0,1) +
                             lastName.substring(0,1);
           System.out.println(initials.toLowerCase();
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
             String expect = "smh";
             boolean passed = getResults(expect, output, "Expected output from main");
             assertTrue(passed);
         }
   
          @Test
         public void testCodeContains()
         {
             String target = ".substring(0,1)";
             boolean passed = checkCodeContains("substring method", target);
             assertTrue(passed);
         }
     }