.. activecode::  ch5Ex9q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-10-practice-coding
   :topics: Unit3-If-Statements/topic-3-10-practice-coding
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T

   Finish the code to print ``It is freezing`` if the temperature is below 30, ``It is cold`` if it is below 50, ``It is nice out`` if it is below 90, or ``It is hot`` using nested if else statements.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           int temp = 100;

       }
   }
   ====
   import static org.junit.Assert.*;
     import org.junit.*;;
     import java.io.*;

     public class RunestoneTests extends CodeTestHelper
     {
          @Test
         public void testCountIfs()
         {
             String code = getCode();
             int num = countOccurences(code, "if");
             boolean passed = num >= 3;

             getResults("3+", "" + num, "Number of if statements", passed);
             assertTrue(passed);
         }

           @Test
         public void testCountElses()
         {
             String code = getCode();
             int num = countOccurences(code, "else");
             boolean passed = num >= 3;

             getResults("3+", "" + num, "Number of else statements", passed);
             assertTrue(passed);
         }

           @Test
         public void testCountPrints()
         {
             String code = getCode();
             int num = countOccurences(code, "System.out.print");
             boolean passed = num >= 4;

             getResults("4+", "" + num, "Number of print statements", passed);
             assertTrue(passed);
         }

         @Test
         public void testMain() throws IOException
         {
           String expect = "It is hot";
           String output = getMethodOutput("main");
           boolean passed = getResults(expect, output, "Prints It is hot if temp = 100");
           assertTrue(passed);
         }
          @Test
         public void testChangedCode() {
             String origCode = "public class Test1 { public static void main(String[] args) {  int temp = 100; } }";
             boolean changed = codeChanged(origCode);
             assertTrue(changed);
         }
     }