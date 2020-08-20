.. activecode:: ArrayListFromArray
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
   :total_students_attempting: 24
   :num_students_correct: 24.0
   :mean_clicks_to_correct: 1.0

   Example code creating an ArrayList from an array.
   ~~~~
   import java.util.*;
   public class ArrayListFromArray
   {
       public static void main(String[] args)
       {
          String[] names = {"Dakota", "Madison", "Brooklyn"};
          ArrayList<String> namesList = new ArrayList<String>(Arrays.asList(names));
          System.out.println(namesList);
       }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("ArrayListFromArray");
        }
   
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "[Dakota, Madison, Brooklyn]";
   
            boolean passed = getResults(expect, output, "main()", true);
            assertTrue(passed);
        }
    }