.. activecode:: ArrayListCreateStr
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: topic-7-1-arraylist-basics
   :topics: Unit7-ArrayList/topic-7-1-arraylist-basics
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 1.0
   :total_students_attempting: 28
   :num_students_correct: 28.0
   :mean_clicks_to_correct: 1.0

   The following code demonstrates a NullPointerException. Change the list2 declaration so that it creates a new Arraylist to remove the NullPointerException.
   ~~~~
   import java.util.*; // import needed for ArrayList
   public class ArrayListCreateStr
   {
       public static void main(String[] args)
       {
          ArrayList<String> nameList = new ArrayList<String>();
          System.out.println("The size of nameList is: " + nameList.size());
          ArrayList<String> list2 = null;
          System.out.println("The size of list2 is: " + list2.size());
       }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("ArrayListCreateStr");
        }
   
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "The size of nameList is: 0\nThe size of list2 is: 0";
   
            boolean passed = getResults(expect, output, "main()", true);
            assertTrue(passed);
        }
     }