.. activecode:: code7_2_4
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

   What does the following code print out? Notice that the array and the target are passed in as arguments to the getIndexOfLastElementSmallerThanTarget method. Trace through it keeping track of the array values and the output. Then run it to see if you're right.  You can also try the code in the |visualizerBF| with the Code Lens button. Can you add another method that finds the index of the last element greater than the target instead of smaller than the target and have main print out a test of it? Call this method getIndexOfLastElementGreaterThanTarget and give it 2 arguments and a return value like the method below.
   ~~~~
   public class ArrayFindSmallest
   {

      /** @return index of the last number smaller than target */
      public static int getIndexOfLastElementSmallerThanTarget(int[ ] values, int target)
      {
         for (int index = values.length - 1; index >= 0; index--)
         {
            if (values[index] < target)
                return index;
         }
         return -1;
      }

      /** Add a method called getIndexOfLastElementGreaterThanTarget
          @param int array
          @param int target
          @return index of the last number greater than target
      */



      public static void main (String[] args)
      {
         int[] theArray = {-30, -5, 8, 23, 46};
         System.out.println("Last index of element smaller than 50: " + getIndexOfLastElementSmallerThanTarget(theArray, 50));
         System.out.println("Last index of element smaller than 30: " + getIndexOfLastElementSmallerThanTarget(theArray, 30));
         System.out.println("Last index of element smaller than 10: " + getIndexOfLastElementSmallerThanTarget(theArray, 10));
         System.out.println("Last index of element smaller than 0: " + getIndexOfLastElementSmallerThanTarget(theArray,0));
         System.out.println("Last index of element smaller than -20: " + getIndexOfLastElementSmallerThanTarget(theArray,-20));
         System.out.println("Last index of element smaller than -30: " + getIndexOfLastElementSmallerThanTarget(theArray,-30));
      }
   }
   ====
   // Test for Lesson 6.2.3 - ArrayFindSmallest

    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("ArrayFindSmallest");
        }

        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "Last index of element smaller than ";

            boolean passed = output.contains(expect);
            output = output.substring(0, output.indexOf("\n"));
            passed = getResults("Last index of element smaller than 50: 4", output, "Ran getIndexOfLastElementSmallerThanTarget", passed);
            assertTrue(passed);
        }


        @Test
        public void test2()
        {
            int[] nums = {10, 50, 20, 30, 40, 20};
            Object[] args = {nums, 30};

            String output = getMethodOutput("getIndexOfLastElementGreaterThanTarget", args);
            String expect = "4";

            boolean passed = getResults(expect, output, "getIndexOfLastElementGreaterThanTarget({10, 50, 20, 30, 40, 20}, 30)");
            assertTrue(passed);
        }

        @Test
        public void test3()
        {
            int[] nums = {10, 50, 20, 30, 40, 20};
            Object[] args = {nums, 100};

            String output = getMethodOutput("getIndexOfLastElementGreaterThanTarget", args);
            String expect = "-1";

            boolean passed = getResults(expect, output, "getIndexOfLastElementGreaterThanTarget({10, 50, 20, 30, 40, 20}, 100)");
            assertTrue(passed);
        }
    }