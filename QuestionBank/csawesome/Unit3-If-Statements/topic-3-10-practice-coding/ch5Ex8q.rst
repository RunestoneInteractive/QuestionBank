.. activecode::  ch5Ex8q
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
   :pct_on_first: 0.7692307692
   :total_students_attempting: 52
   :num_students_correct: 48.0
   :mean_clicks_to_correct: 1.2083333333

   Finish the following code so that it prints ``You have a fever`` if your temperature is above 100 and otherwise prints ``You don't have a fever``.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           double temp = 103.5;
       }
   }
   ====
   import static org.junit.Assert.*;
     import org.junit.*;;
     import java.io.*;
   
     public class RunestoneTests extends CodeTestHelper
     {
         @Test
         public void testCheckCodeContains()
         {
             boolean output1 = checkCodeContains("print statement You have a fever", "System.out.println(\"You have a fever\")");
             assertTrue(output1);
         }
   
         @Test
         public void testCheckCodeContains2()
         {
             boolean output2 = checkCodeContains("print statement You don't have a fever", "System.out.println(\"You don't have a fever\")");
             assertTrue(output2);
         }
   
         @Test
         public void testCheckCodeContains3()
         {
             boolean output4 = checkCodeContains("if statement for temp greater than 100", "if (temp > 100)");
             assertTrue(output4);
         }
   
          @Test
         public void testChangedCode() {
             String origCode = "public class Test1 { public static void main(String[] args) { double temp = 103.5; } }";
             boolean changed = codeChanged(origCode);
             assertTrue(changed);
         }
     }