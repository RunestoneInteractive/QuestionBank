.. activecode:: arrayListRemoveInLoop
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: topic-7-4-arraylist-algorithms
   :topics: Unit7-ArrayList/topic-7-4-arraylist-algorithms
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 16
   :num_students_correct: 16.0
   :mean_clicks_to_correct: 1.0

   The following code is supposed to initialize the ArrayList arr to [0,1,2,3,4] and then remove every other element to get [1,3]. However, when you remove an element the size of the array changes and elements move up an index! See if you can figure out why you get the unexpected result. Try the CodeLens button to trace through the code.
   ~~~~
   import java.util.*;
   
   public class ArrayListLoop
   {
    public static void main(String[] args)
    {
      ArrayList<Integer> arr = new ArrayList<Integer>();
      for(int i=0; i < 5; i++)
      {
         arr.add(i);
   
      }
      for(int i=0; i < arr.size(); i++)
      {
         if (i % 2 == 0)
         {
            System.out.println("Removing element " + i + " : " + arr.get(i));
            arr.remove(i);
         }
      }
      System.out.println(arr);
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
            String expect = "Removing element 0: 0\nRemoving element 2: 3\n[1, 2, 4]";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }