.. activecode::  ooEx7q
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

   Add a call to Pet's brag method before printing anything in Dog's brag method (hint: use super to call an overridden method).  It should print ``I have the best pet!`` and then ``I have the best dog``.
   ~~~~
   public class Pet
   {
   
       public void brag()
       {
           System.out.println("I have the best pet!");
       }
   
       public static void main(String[] args)
       {
           Dog d1 = new Dog();
           d1.brag();
       }
   }
   
   class Dog extends Pet
   {
       public void brag()
       {
           // ADD CODE HERE
   
           System.out.println("I have the best dog!");
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
        String expect = "I have the best pet!\n" +
                        "I have the best dog!\n";
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
   
   
      @Test
      public void test1()
      {
        String target = "super.brag();";
        boolean passed = checkCodeContains("super to override method brag", target);
        assertTrue(passed);
      }
    }