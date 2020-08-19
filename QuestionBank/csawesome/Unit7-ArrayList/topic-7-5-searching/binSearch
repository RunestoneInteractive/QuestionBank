.. activecode:: binSearch
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit7-ArrayList
  :subchapter: topic-7-5-searching
  :topics: Unit7-ArrayList/topic-7-5-searching
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 1.0
  :total_students_attempting: 20
  :num_students_correct: 20.0
  :mean_clicks_to_correct: 1.0

  Demonstration of iterative binary search. Click on the Code Lens button or the link below to step through this code.
  ~~~~
  public class SearchTest
  {
     public static int binarySearch(int[] elements, int target) {
        int left = 0;
        int right = elements.length - 1;
        while (left <= right)
        {
           int middle = (left + right) / 2;
           if (target < elements[middle])
           {
              right = middle - 1;
           }
           else if (target > elements[middle])
           {
              left = middle + 1;
           }
           else {
              return middle;
           }
         }
         return -1;
     }
  
     public static void main(String[] args)
     {
        int[] arr1 = {-20, 3, 15, 81, 432};
  
        // test when the target is in the middle
        int index = binarySearch(arr1,15);
        System.out.println(index);
  
        // test when the target is the first item in the array
        index = binarySearch(arr1,-20);
        System.out.println(index);
  
        // test when the target is in the array - last
        index = binarySearch(arr1,432);
        System.out.println(index);
  
        // test when the target is not in the array
        index = binarySearch(arr1,53);
        System.out.println(index);
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
            String expect = "2\n0\n4\n-1";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }