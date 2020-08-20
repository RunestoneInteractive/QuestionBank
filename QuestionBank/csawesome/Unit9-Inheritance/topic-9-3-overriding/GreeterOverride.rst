.. activecode:: GreeterOverride
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: topic-9-3-overriding
   :topics: Unit9-Inheritance/topic-9-3-overriding
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.0
   :total_students_attempting: 12
   :num_students_correct: 7.0
   :mean_clicks_to_correct: 3.4285714286

   After running the code, try overriding the greet(String) method in the MeanGreeter class to return ``Go away`` + the who String.
   ~~~~
   public class Greeter
   {
      public String greet()
      {
         return "Hi";
      }
   
      public String greet(String who)
      {
         return "Hello " + who;
      }
   
      public static void main(String[] args)
      {
         Greeter g1 = new Greeter();
         System.out.println(g1.greet("Sam"));
         Greeter g2 = new MeanGreeter();
         System.out.println(g2.greet("Nimish"));
      }
   }
   
   class MeanGreeter extends Greeter
   {
      public String greet()
      {
         return "Go away";
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
      public RunestoneTests(){
        super("Greeter");
      }
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "Hello Sam\nGo away Nimish";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
   
        @Test
        public void testCodeContains(){
         String code = removeSpaces(getCode());
         String target = removeSpaces("public String greet(String");
   
         int num = countOccurences(code, target);
         boolean passed = num >= 2;
         getResults("2", ""+num, "Testing code for  number of greet methods");
         assertTrue(passed);
        }
    }