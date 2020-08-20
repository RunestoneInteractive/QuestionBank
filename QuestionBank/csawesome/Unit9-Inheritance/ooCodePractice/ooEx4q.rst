.. activecode::  ooEx4q
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

   Add an equals method to this class that returns true if the current Dog and passed Dog have the same name.  The code should print false twice then true twice.
   ~~~~
   public class Dog
   {
       private String name;
   
       public Dog(String name)
       {
           this.name = name;
       }
   
       public boolean equals(Object other)
       {
           // ADD CODE HERE
       }
   
       public static void main(String[] args)
       {
           Dog d1 = new Dog("Rufus");
           Dog d2 = new Dog("Sally");
           Dog d3 = new Dog("Rufus");
           Dog d4 = d3;
           System.out.println(d1.equals(d2));
           System.out.println(d2.equals(d3));
           System.out.println(d1.equals(d3));
           System.out.println(d3.equals(d4));
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
        String expect = "false\n" +
                        "false\n" +
                        "true\n" +
                        "true\n" ;
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
   
    @Test
      public void test1()
      {
        String target = "Dog * = (Dog)other";
   
        boolean passed = checkCodeContainsRegex("casting of Object other to type Dog", target);
        assertTrue(passed);
      }
   
    @Test
      public void test2()
      {
        Dog d1 = new Dog("Rufus");
        Dog d2 = new Dog("Sally");
   
        String result = String.valueOf(!(d1.equals(d2)));
   
        boolean passed = getResults("true", result, "Equals method test - not equals");
        assertTrue(passed);
      }
   
      @Test
      public void test3()
      {
        Dog d1 = new Dog("Rufus");
        Dog d3 = new Dog("Rufus");
   
        String result = String.valueOf((d1.equals(d3)));
   
        boolean passed = getResults("true", result, "Equals method test - equals");
        assertTrue(passed);
      }
    }