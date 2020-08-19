.. activecode:: code7_2_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit7-Arrays
   :subchapter: topic-7-2-traversing-arrays
   :topics: Unit7-Arrays/topic-7-2-traversing-arrays
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T

   What will the following code print out? Can you write a similar method called tripleFirstFour() that triples the first 4 elements of the array? Make sure you test it in main.
   ~~~~
   public class ArrayWorker
   {

      /** Doubles the first 5 elements of the array */
      public static void doubleFirstFive(int[] values)
      {
        // Notice: && i < 5
        for (int i = 0; i < values.length && i < 5; i++)
        {
          values[i] = values[i] * 2;
        }
      }

      /** Write a method called tripleFirstFour() that triples the first 4 elements of the array **/



      public static void printArray(int[] values)
      {
        for (int i = 0; i < values.length; i++)
         {
           System.out.println(  values[i] );
         }
      }

      public static void main(String[] args)
      {
        int[] numArray = {3, 8, -3, 2, 20, 5, 33, 1};
        doubleFirstFive(numArray);
        printArray(numArray);
      }
   }
   ====
   // Test for Lesson 6.2.4 - ArrayWorker

    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("ArrayWorker");

            int[] numArray = {0, 1, 2, 3, 4, 5};
            setDefaultValues(new Object[]{numArray});
        }

        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "6 16 -6 4 40 5 33 1".replaceAll(" ", "\n");

            boolean passed = output.contains(expect);

            passed = getResults(expect, output, "Did you run the doubleFirstFiveMethod?", passed);
            assertTrue(passed);
        }

        @Test
        public void test2()
        {
            String output = getMethodOutput("tripleFirstFour");
            output = getMethodOutput("printArray");
            String expect = "0 3 6 9 4 5".replaceAll(" ", "\n");

            boolean passed = output.contains(expect);

            passed = getResults(expect, output, "Testing tripleFirstFour() method on array [0, 1, 2, 3, 4, 5]", passed);
            assertTrue(passed);
        }
    }