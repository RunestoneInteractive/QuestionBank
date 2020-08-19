.. activecode:: insertionSort
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit7-ArrayList
  :subchapter: topic-7-6-sorting
  :topics: Unit7-ArrayList/topic-7-6-sorting
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 1.0
  :total_students_attempting: 20
  :num_students_correct: 20.0
  :mean_clicks_to_correct: 1.0

  Demonstration of insertion sort. Click on the Code Lens button or the link below to step through the code.
  ~~~~
  import java.util.Arrays;
  
  public class SortTest
  {
     public static void insertionSort(int[] elements)
     {
        for (int j = 1; j < elements.length; j++)
        {
           int temp = elements[j];
           int possibleIndex = j;
           while (possibleIndex > 0 && temp < elements[possibleIndex - 1])
           {
              elements[possibleIndex] = elements[possibleIndex - 1];
              possibleIndex--;
           }
           elements[possibleIndex] = temp;
        }
    }
  
     public static void main(String[] args)
     {
        int[] arr1 = {3, 86, -20, 14, 40};
        System.out.println(Arrays.toString(arr1));
        insertionSort(arr1);
        System.out.println(Arrays.toString(arr1));
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
            String expect = "[3, 86, -20, 14, 40]\n[-20, 3, 14, 40, 86]";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }