.. activecode:: selSort
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
  :total_students_attempting: 23
  :num_students_correct: 23.0
  :mean_clicks_to_correct: 1.0

  Demonstration of selection sort. Click on the Code Lens button or the link below to step through the code.
  ~~~~
  import java.util.Arrays;
  
  public class SortTest
  {
     public static void selectionSort(int[] elements)
     {
        for (int j = 0; j < elements.length - 1; j++)
        {
           int minIndex = j;
           for (int k = j + 1; k < elements.length; k++)
           {
              if (elements[k] < elements[minIndex])
              {
                 minIndex = k;
              }
           }
           int temp = elements[j];
           elements[j] = elements[minIndex];
           elements[minIndex] = temp;
         }
     }
  
     public static void main(String[] args)
     {
        int[] arr1 = {3, 86, -20, 14, 40};
        System.out.println(Arrays.toString(arr1));
        selectionSort(arr1);
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