.. activecode:: parallelArrayLists
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
   :total_students_attempting: 15
   :num_students_correct: 15.0
   :mean_clicks_to_correct: 1.0

   Demonstration of parallel ArrayLists.
   ~~~~
   import java.util.*;
   
    public class ParallelTests
    {
        public static void main(String[] args)
        {
            ArrayList<Integer> test1Grades = new ArrayList<Integer>();
            ArrayList<Integer> test2Grades = new ArrayList<Integer>();
            test1Grades.add(100);
            test2Grades.add(100);
            test1Grades.add(80);
            test2Grades.add(70);
            test1Grades.add(70);
            test2Grades.add(90);
            double total = 0;
            for (int i = 0; i < test1Grades.size(); i++)
            {
                total +=  test1Grades.get(i) + test2Grades.get(i);
            }
            int numberOfGrades = test1Grades.size() * 2;
            System.out.println("Average over two tests: " + total/numberOfGrades);
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
            String expect = "Average over two tests: 85.0";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
    }