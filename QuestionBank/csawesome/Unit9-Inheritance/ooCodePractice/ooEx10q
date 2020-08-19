.. activecode::  ooEx10q
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

   Correctly finish the Dog subclass for the following Animal class.  Override the methods speak() to print ``woof`` and eat() to print ``num num``.
   ~~~~
   class Animal
   {
       public String name;
       public int numLegs;
       public void speak() { System.out.println("sniff");}
       public void eat() { System.out.println("crunch"); }
   }
   
   public class Dog extends Animal
   {
       // ADD CODE HERE
   
       public static void main(String[] args)
       {
           Dog myDog = new Dog();
           myDog.speak();
           myDog.eat();
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
        String expect = "woof\n" +
                        "num num\n";
   
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
   
      @Test
      public void test1()
      {
        String target = " public void speak()";
        boolean passed = checkCodeContains("speak method", target);
        assertTrue(passed);
      }
   
      @Test
      public void test2()
      {
        String target = " public void eat()";
        boolean passed = checkCodeContains("eat method", target);
        assertTrue(passed);
      }
    }