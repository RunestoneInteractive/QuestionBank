.. activecode:: divideby10
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit8-ArrayList
   :subchapter: topic-8-1-arraylist-basics
   :topics: Unit8-ArrayList/topic-8-1-arraylist-basics
   :from_source: T
   :language: java
   :autograde: unittest

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