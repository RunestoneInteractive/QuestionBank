.. activecode:: listForLoop
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: topic-7-3-arraylist-loops
   :topics: Unit7-ArrayList/topic-7-3-arraylist-loops
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.4347826087
   :total_students_attempting: 23
   :num_students_correct: 15.0
   :mean_clicks_to_correct: 1.3333333333

   The following code will throw an ArrayIndexOutOfBoundsException. Can you fix it?
   ~~~~
   import java.util.*;
   public class TestForLoop
   {
       public static void main(String[] args)
       {
           ArrayList<Integer> myList = new ArrayList<Integer>();
           myList.add(50);
           myList.add(30);
           myList.add(20);
           int total = 0;
           for (int i=0; i <= myList.size(); i++)
           {
               total = total + myList.get(i);
           }
           System.out.println(total);
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
            String expect = "100";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
        @Test
        public void fixedCode()
        {
          boolean passed = checkCodeContains("fixed test in loop", "i < myList.size()");
          assertTrue(passed);
        }
    }