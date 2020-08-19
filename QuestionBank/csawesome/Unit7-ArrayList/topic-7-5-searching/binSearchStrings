.. activecode:: binSearchStrings
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

  Demonstration of binary search with strings using compareTo. Click on the Code Lens button to step through the code.
  ~~~~
  public class BinSearchStrings
  {
     public static int binarySearch(String[] elements, String target) {
        int left = 0;
        int right = elements.length - 1;
        while (left <= right)
        {
           int middle = (left + right) / 2;
           if (target.compareTo(elements[middle]) < 0)
           {
              right = middle - 1;
           }
           else if (target.compareTo(elements[middle]) > 0)
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
        String[] arr1 = {"apple","banana","cherry","kiwi","melon"};
  
        // test when the target is in the middle
        int index = binarySearch(arr1,"cherry");
        System.out.println(index);
  
        // test when the target is the first item in the array
        index = binarySearch(arr1,"apple");
        System.out.println(index);
  
        // test when the target is in the array - last
        index = binarySearch(arr1,"melon");
        System.out.println(index);
  
        // test when the target is not in the array
        index = binarySearch(arr1,"pear");
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