.. activecode::  ch5Ex6q
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
   :pct_on_first: 0.5740740741
   :total_students_attempting: 54
   :num_students_correct: 49.0
   :mean_clicks_to_correct: 1.7346938776

   Finish the code below so that it prints ``You can go out`` if you have a ride or if you can walk and otherwise prints ``You can't go out``.  Use a logical or to create a complex conditional.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           boolean canWalk = true;
           boolean haveRide = false;
   
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
             boolean output2 = checkCodeContains("print statement You can't go out", "System.out.println(\"You can't go out\")");
             assertTrue(output2);
         }
   
         @Test
         public void testCheckCodeContains3()
         {
             boolean output3 = checkCodeContains("or", "||");
             assertTrue(output3);
         }
   
           @Test
         public void testChangedCode() {
             String origCode = "public class Test1 { public static void main(String[] args) { boolean canWalk = true; boolean haveRide = false; } }";
   
             boolean changed = codeChanged(origCode);
   
             assertTrue(changed);
   
         }
     }