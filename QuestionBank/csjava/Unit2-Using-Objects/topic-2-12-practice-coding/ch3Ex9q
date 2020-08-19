.. activecode::  ch3Ex9q
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

   Write the code to print a random number from 1 to 100.  You can use ``Math.random()`` to get a value between 0 and not quite 1.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {

       }
   }
   ====
   import static org.junit.Assert.*;
     import org.junit.*;;
     import java.io.*;

     public class RunestoneTests extends CodeTestHelper
     {
         @Test
         public void testCheckCodeContains1()
         {
             boolean passed = checkCodeContainsNoRegex("random number up to 100", "Math.random()*100");
             assertTrue(passed);
         }

          @Test
         public void testCheckCodeContains2()
         {
             boolean passed = checkCodeContainsNoRegex("random number starting at 1", "+1");
             assertTrue(passed);
         }

          @Test
         public void testCheckCodeContains3()
         {
             boolean passed = checkCodeContains("casting to int", "(int)");
             assertTrue(passed);
         }
     }