.. activecode:: divideby10
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: topic-7-1-arraylist-basics
   :topics: Unit7-ArrayList/topic-7-1-arraylist-basics
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.2105263158
   :total_students_attempting: 57
   :num_students_correct: 50.0
   :mean_clicks_to_correct: 1.9

   Set number to a different number and guess what number / and % will return. Which operator gives you a digit in number?
   ~~~~
   public class DivideBy10
   {
      public static void main(String[] args)
      {
         int number = 154;
         System.out.println(number / 10);
         System.out.println(number % 10);
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("DivideBy10");
        }
   
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "15\n4";
   
            boolean passed = !output.equals(expect);
   
            passed = getResults(expect, output, "Try another number", passed);
            assertTrue(passed);
        }
    }