.. activecode:: seqSearch
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
  :total_students_attempting: 23
  :num_students_correct: 23.0
  :mean_clicks_to_correct: 1.0

  The code for ``sequentialSearch`` for arrays below is from a previous AP CS A course description. Click on the Code Lens button or the link below to see this code running in the Java visualizer.
  ~~~~
  public class ArraySearcher
  {
  
     /** Finds the index of a value in an array of integers.
       * @param elements an array containing the items to be searched.
       * @param target the item to be found in elements.
       * @return an index of target in elements if found; -1 otherwise.
       */
     public static int sequentialSearch(int[] elements, int target)
     {
       for (int j = 0; j < elements.length; j++)
       {
         if (elements[j] == target)
         {
           return j;
         }
       }
       return -1;
     }
  
     public static void main(String[] args)
     {
       int[] numArray = {3, -2, 9, 38, -23};
       System.out.println("Tests of sequentialSearch");
       System.out.println(sequentialSearch(numArray,3));
       System.out.println(sequentialSearch(numArray,9));
       System.out.println(sequentialSearch(numArray,-23));
       System.out.println(sequentialSearch(numArray,99));
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
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }