.. activecode::  ooEx12q
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
   :total_students_attempting: 3
   :num_students_correct: 3.0
   :mean_clicks_to_correct: 1.0

   Override the Person class's speak function inside the Student class. Make the function print ``I'm a student``.
   ~~~~
   public class Person
   {
       public void speak()
       {
           System.out.println("I'm a person");
       }
   
       public static void main(String[] args)
       {
           Person p1 = new Student();
           p1.speak();
       }
   }
   
   class Student extends Person
   {
       // ADD CODE HERE
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
        String expect = "I'm a student\n";
   
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
   
    @Test
      public void test1()
      {
        String code = getCode();
        String target = "public void speak()";
   
        int num = countOccurencesRegex(code, target);
   
        boolean passed = (num == 2);
   
        getResults("2", ""+num, "2 speak methods", passed);
        assertTrue(passed);
      }
    }