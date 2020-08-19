.. activecode:: seqSearchList
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

    Here is a linear search using ArrayLists. Notice that size() and get(i) is used with ArrayLists instead of length and [i] which are used in arrays. Click on the Code Lens button to step through this code in the visualizer.
    ~~~~
    import java.util.*;
    
    public class ArrayListSearcher
    {
    
      /** Finds the index of a value in an ArrayList of integers.
        * @param elements an array containing the items to be searched.
        * @param target the item to be found in elements.
        * @return an index of target in elements if found; -1 otherwise.
        */
      public static int sequentialSearch(ArrayList<Integer> elements, int target)
      {
        for (int j = 0; j < elements.size(); j++)
        {
          if (elements.get(j) == target)
          {
            return j;
          }
        }
        return -1;
      }
    
      public static void main(String[] args)
      {
        ArrayList<Integer> numList = new ArrayList<Integer>();
        numList.add(3);
        numList.add(-2);
        numList.add(9);
        numList.add(38);
        numList.add(-23);
        System.out.println("Tests of sequentialSearch");
        System.out.println(sequentialSearch(numList,3));
        System.out.println(sequentialSearch(numList,9));
        System.out.println(sequentialSearch(numList,-23));
        System.out.println(sequentialSearch(numList,99));
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
            String expect = "Tests of sequentialSearch\n0\n2\n4\n-1";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
    }