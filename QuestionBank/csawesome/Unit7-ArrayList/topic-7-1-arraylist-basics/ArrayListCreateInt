.. activecode:: ArrayListCreateInt
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: topic-7-1-arraylist-basics
   :topics: Unit7-ArrayList/topic-7-1-arraylist-basics
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 29
   :num_students_correct: 29.0
   :mean_clicks_to_correct: 1.0

   Here's an example of a Integer ArrayList.
   ~~~~
   import java.util.*; // import everything at this level
   public class ArrayListCreateInt
   {
       public static void main(String[] args)
       {
          ArrayList<Integer> numList = new ArrayList<Integer>();
          System.out.println(numList.size());
       }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("ArrayListCreateInt");
        }
   
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "0";
   
            boolean passed = getResults(expect, output, "main()", true);
            assertTrue(passed);
        }
    }