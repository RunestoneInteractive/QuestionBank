.. activecode:: ooEx3q
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

   Edit this code so the class Beagle is a subclass of the Dog class.  When you run the code it should print "woof!" and then "arf arf".
   ~~~~
   public class Dog
   {
       public void speak()
       {
           System.out.println("woof!");
       }
   
       public static void main(String[] args)
       {
           Dog d = new Dog();
           d.speak();
           Dog b = new Beagle();
           b.speak();
       }
   }
   
   class Beagle
   {
       public void speak()
       {
           System.out.println("arf arf");
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
        String expect = "woof!\n" +
                        "arf arf\n";
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
   
   
    @Test
      public void testBeagleExtendsDog()
      {
        String target = "class Beagle extends Dog";
        boolean passed = checkCodeContains("class Beagle extends class Dog",target);
        assertTrue(passed);
      }
    }