.. activecode:: GreeterEx
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: topic-9-3-overriding
   :topics: Unit9-Inheritance/topic-9-3-overriding
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.25
   :total_students_attempting: 12
   :num_students_correct: 6.0
   :mean_clicks_to_correct: 1.8333333333

   Add another subclass called SpanishGreeter (or another language that you know) that extends Greeter and override the greet() method to return ``Hola!`` (or hi in another language) instead of ``Hi!``. Create an object to test it out.
   ~~~~
   public class Greeter
   {
      public String greet()
      {
         return "Hi";
      }
   
      public static void main(String[] args)
      {
         Greeter g1 = new Greeter();
         System.out.println(g1.greet());
         Greeter g2 = new MeanGreeter();
         System.out.println(g2.greet());
      }
   }
   
   class MeanGreeter extends Greeter
   {
      public String greet()
      {
         return "Go Away";
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
        public void testChangedCode() {
            String origCode = "public static void main(String[] args) { Greeter g1 = new Greeter(); System.out.println(g1.greet()); Greeter g2 = new MeanGreeter() System.out.println(g2.greet()); }";
   
            boolean changed = codeChanged(origCode);
   
            assertTrue(changed);
   
        }
   
        @Test
        public void test2()
        {
            String code = getCode();
            String target = "extends Greeter";
   
            int num = countOccurences(code, target);
   
            boolean passed = num >= 2;
            getResults("2", ""+num, "Testing code for " + target);
            assertTrue(passed);
        }
   
        @Test
        public void test3()
        {
            String code = getCode();
            String target = "public String greet()";
   
            int num = countOccurences(code, target);
   
            boolean passed = num >= 3;
            getResults("3", ""+num, "Testing code for " + target);
            assertTrue(passed);
        }
   
        @Test
        public void test4()
        {
            String code = getCode();
            String target = ".greet()";
   
            int num = countOccurences(code, target);
   
            boolean passed = num >= 3;
            getResults("3", ""+num, "Testing code for " + target);
            assertTrue(passed);
        }
    }