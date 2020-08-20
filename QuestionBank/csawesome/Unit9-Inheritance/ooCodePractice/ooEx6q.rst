.. activecode::  ooEx6q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: ooCodePractice
   :topics: Unit9-Inheritance/ooCodePractice
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 1.0

   Overload the greet method to just print ``Hello`` if not given any parameters.  It should print ``Hello`` and then ``Hello Sansa``.
   ~~~~
   public class Student
   {
       public static void greet(String name)
       {
           System.out.println("Hello " + name);
       }
   
       public static void main(String[] args)
       {
          greet();
          greet("Sansa");
       }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;
    import java.util.List;
    import java.util.ArrayList;
   
    public class RunestoneTests extends CodeTestHelper
    {
   
      @Test
      public void testMain() throws IOException
      {
        String output = getMethodOutput("main");
        String expect = "Hello\nHello Sansa";
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
   
   
      @Test
      public void test1()
      {
        String target = "greet();";
        boolean passed = checkCodeContains("overriden greet method", target);
        assertTrue(passed);
      }
    }