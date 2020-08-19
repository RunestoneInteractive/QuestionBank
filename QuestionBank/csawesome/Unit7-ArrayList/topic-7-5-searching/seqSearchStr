.. activecode:: seqSearchStr
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
  :total_students_attempting: 21
  :num_students_correct: 21.0
  :mean_clicks_to_correct: 1.0

  Demonstration of a linear search for a String. Click on the Code Lens button or the link below to step through this code.
  ~~~~
  public class SearchTest
  {
  
     public static int sequentialSearch(String[] elements, String target)
     {
        for (int j = 0; j < elements.length; j++)
        {
           if (elements[j].equals(target))
           {
              return j;
           }
       }
       return -1;
     }
  
     public static void main(String[] args)
     {
        String[] arr1 = {"blue", "red", "purple", "green"};
  
        // test when the target is in the array
        int index = sequentialSearch(arr1,"red");
        System.out.println(index);
  
        // test when the target is not in the array
        index = sequentialSearch(arr1,"pink");
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
            String expect = "1\n-1";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }