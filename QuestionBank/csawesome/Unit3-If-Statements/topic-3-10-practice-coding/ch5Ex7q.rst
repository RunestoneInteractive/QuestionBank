.. activecode::  ch5Ex7q
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
   :pct_on_first: 0.5535714286
   :total_students_attempting: 56
   :num_students_correct: 50.0
   :mean_clicks_to_correct: 1.78

   Finish the code below to print you can go out if you don't have homework and you have done the dishes.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           boolean haveHomework = false;
           boolean didDishes = true;
   
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
             boolean output1 = checkCodeContains("print statement You can go out", "System.out.println(\"You can go out\")");
             assertTrue(output1);
         }
   
         @Test
         public void testCheckCodeContains2()
         {
             boolean output2 = checkCodeContains("and", "&&");
             assertTrue(output2);
         }
   
         @Test
         public void testCheckCodeContains3()
         {
             boolean output2 = checkCodeContains("not", "!");
             assertTrue(output2);
         }
   
          @Test
         public void testChangedCode() {
             String origCode = "public class Test1 { public static void main(String[] args) { boolean haveHomework = false; boolean didDishes = true; } }";
             boolean changed = codeChanged(origCode);
             assertTrue(changed);
         }
     }