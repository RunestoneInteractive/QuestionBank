.. activecode::  ooEx1q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: ooCodePractice
   :topics: Unit9-Inheritance/ooCodePractice
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.3333333333
   :total_students_attempting: 3
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 1.5

   Write a method that overloads the talk method by taking in a name and printing ``Hello`` with that name.
   ~~~~
   public class Test1
   {
       public static void talk()
       {
             System.out.println("hello there!");
       }
   
       public static // FINISH THE METHOD HERE //
   
       public static void main(String[] args)
       {
             talk("Matthew");
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
        String expect = "Hello Matthew\n";
   
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
   
    @Test
      public void testtalk_name()
      {
        String target = "public static void talk(String *)";
        boolean passed = checkCodeContainsRegex("overloaded method talk with a String parameter",target);
        assertTrue(passed);
      }
    }