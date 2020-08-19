.. activecode::  arr2DEx8q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: Array2dCodePractice
   :topics: Unit8-2DArray/Array2dCodePractice
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.7586206897
   :total_students_attempting: 29
   :num_students_correct: 29.0
   :mean_clicks_to_correct: 1.4482758621

   Replace the "ADD CODE HERE" below with the code to count and print the number of 7's that are in the 2d array. It should print 2.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           int[][] array = { {4,7,8},{8,8,7} };
   
           //ADD CODE HERE
   
       }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "2";
             boolean passed = output.contains(expect);
              getResults(expect, output, "Expected output from main", passed);
            assertTrue(passed);
        }
        @Test
        public void test1()
        {
            String target = "for";
            int num = countOccurences(getCode(), target);
            boolean passed = (num == 2);
            getResults("2", num+"","2 for loops",passed);
            assertTrue(passed);
        }
        @Test
        public void test2()
        {
            String target = "if (array[*][*] == 7)";
            boolean passed = checkCodeContains("if statement checking if array[*][*] element equals 7", target);
            assertTrue(passed);
        }
    }