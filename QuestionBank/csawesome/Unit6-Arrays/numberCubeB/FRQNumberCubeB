.. activecode:: FRQNumberCubeB
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: numberCubeB
   :topics: Unit6-Arrays/numberCubeB
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.5
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 4.5

   FRQ Number Cube B: Write the method ``getLongestRun`` that takes as its parameter an array of integer values representing a series of number cube tosses. The method returns the starting index in the array of a run of maximum size. A run is defined as the repeated occurrence of the same value in two or more consecutive positions in the array.
   ~~~~
   public class NumberCube
   {
   
       public static int getLongestRun(int[] values)
       {
           // Complete this method
       }
   
       public static void main(String[] args){
           int[] values = {3, 5, 6, 6, 3, 6, 4, 4, 4, 2, 6, 4, 1, 1, 1, 1};
           int longestRunIdx = getLongestRun(values);
   
           if(longestRunIdx != 12){
              System.out.println("Your code does not return the correct index.");
   
              if(longestRunIdx == 2 || longestRunIdx == 6)
                  System.out.println("It is returning the start index of a run, but that run is not the longest.");
   
              System.out.println("Remember that your code must return the start index of the longest run of tosses.");
           } else {
              System.out.println("Looks like your code works well!");
           }
       }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;
    import java.util.Arrays;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void test1()
        {
            String expect = "Looks like your code works well!";
            String actual = getMethodOutput("main");
   
            boolean passed = getResults(expect, actual, "Checking output of main()");
            assertTrue(passed);
        }
   
        @Test
        public void test2() {
            int[] values = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
   
            String actual = "" + NumberCube.getLongestRun(values);
            String expect = "-1";
   
            boolean passed = getResults(expect, actual, "Checking output with " + Arrays.toString(values));
            assertTrue(passed);
        }
   
        @Test
        public void test3() {
            int[] values = {1, 1, 1, 1, 1, 1, 1, 1, 1};
   
            String actual = "" + NumberCube.getLongestRun(values);
            String expect = "0";
   
            boolean passed = getResults(expect, actual, "Checking output with " + Arrays.toString(values));
            assertTrue(passed);
        }
   
        @Test
        public void test4() {
            int[] values = {1, 1, 1, 1, 2, 2, 2, 2, 2};
   
            String actual = "" + NumberCube.getLongestRun(values);
            String expect = "4";
   
            boolean passed = getResults(expect, actual, "Checking output with " + Arrays.toString(values));
            assertTrue(passed);
        }
    }