.. activecode:: StringTest1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: topic-9-7-Object
   :topics: Unit9-Inheritance/topic-9-7-Object
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 6
   :num_students_correct: 6.0
   :mean_clicks_to_correct: 1.0

   Try to guess what this code will print out before running it.
   ~~~~
   public class StringTest
   {
      public static void main(String[] args)
      {
         String s1 = "hi";
         String s2 = "Hi";
         String s3 = new String("hi");
         System.out.println(s1.equals(s2));
         System.out.println(s2.equals(s3));
         System.out.println(s1.equals(s3));
      }
   }
   ====
   import static org.junit.Assert.*;
     import org.junit.*;
     import java.io.*;
   
     public class RunestoneTests extends CodeTestHelper
     {
         public RunestoneTests() {
             super("StringTest");
         }
   
         @Test
         public void test1()
         {
             String output = getMethodOutput("main");
             String expect = "false\nfalse\ntrue";
   
             boolean passed = getResults(expect, output, "Checking output from main()", true);
             assertTrue(passed);
   
         }
     }