.. activecode:: code7_3_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit7-Arrays
   :subchapter: topic-7-3-arrays-with-foreach
   :topics: Unit7-Arrays/topic-7-3-arrays-with-foreach
   :from_source: T
   :language: java
   :autograde: unittest

   Try the code below.
   ~~~~
   public class ArrayWorker
   {

      public static double getAverage(int[] values)
      {
        double total = 0;
        for (int val : values)
        {
          total  = total + val;
        }
        return total / values.length;
      }

      public static void main(String[] args)
      {
        int[] numArray =  {2, 6, 7, 12, 5};
        System.out.println(getAverage(numArray));
      }
   }
   ====
   // Test for Lesson 6.3.3 - IncrementLoop

    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("ArrayWorker");
        }

        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "6.4";

            boolean passed = getResults(expect, output, "main()", true);
            assertTrue(passed);
        }
    }