.. activecode::  arr2DEx3q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: Array2dCodePractice
   :topics: Unit8-2DArray/Array2dCodePractice
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.8666666667
   :total_students_attempting: 30
   :num_students_correct: 30.0
   :mean_clicks_to_correct: 1.1666666667

   Print the values 47, 51, and 20 by accessing them in  the given two-dimensional array.
   ~~~~
   public class Test1
   {
       public static void main(String[] args)
       {
           int[][] arr = { {47,3,12},{51,74,20} };
   
           // ADD CODE HERE //
   
       }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testDigitOne() throws IOException
        {
            String target = "arr[0][0]";
            boolean passed = checkCodeContains("using arr to access 47", target);
           assertTrue(passed);
        }
        @Test
        public void testDigit2() throws IOException
        {
            String target = "arr[1][0]";
            boolean passed = checkCodeContains("using arr to access 51", target);
           assertTrue(passed);
        }
        @Test
        public void testDigit3() throws IOException
        {
            String target = "arr[1][2]";
            boolean passed = checkCodeContains("using arr to access 20", target);
           assertTrue(passed);
        }
    }